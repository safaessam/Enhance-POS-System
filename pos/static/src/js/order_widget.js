/** @odoo-module **/
import { OrderWidget } from "@point_of_sale/app/generic_components/order_widget/order_widget";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";
import { rpc } from "@web/core/network/rpc";

patch(OrderWidget.prototype, {
    setup() {
        super.setup();
        this.dialog = useService("dialog");
        this.pos = useService("pos");
        this.notification = useService("notification");
        this.busService = this.env.services.bus_service;


    },

    get waiter() {
        return this.props.order?.get_waiter?.() || null;
        console.log("Waiter:", this.waiter);
    },

   async onClickWaiterButton() {
    try {
        await this.pos.ready;

        // Safely load employees with null checks and ensure is_waiter is loaded

        const allEmployees = this.pos.models['hr.employee'] || [];

        // Ensure that we map the employee data correctly
        const employeesWithWaiterStatus = allEmployees.map(employee => ({
            id: employee.id,
            name: employee.name,
//            is_waiter: employee.is_waiter // will be undefined if not loaded
            is_waiter: Boolean(employee.is_waiter) // Ensure it's a boolean
        }));

        console.log("Employees with waiter status:", employeesWithWaiterStatus);

        // Filter only waiters
        const waiters = employeesWithWaiterStatus.filter(employee => employee.is_waiter === true);

        if (!waiters.length) {
            this.notification.add(
                _t("No waiters available. Please configure waiters first."),
                { type: 'warning', sticky: true }
            );
            return;
        }

        const currentWaiterId = this.waiter?.id;
        const selectedWaiterId = currentWaiterId || waiters[0]?.id;

        // Create safe selection dialog
        const confirmed = await this._showWaiterSelectionDialog(waiters, selectedWaiterId);

        if (confirmed && selectedWaiterId) {
            const waiter = waiters.find(w => w?.id === selectedWaiterId);
            if (waiter) {
                await this._assignWaiterToOrder(waiter);
            }
        }
    } catch (error) {
        console.error("Waiter selection error:", error);
        this.notification.add(
            _t("Error assigning waiter: %s", error.message),
            { type: 'danger' }
        );
    }
},

    async _showWaiterSelectionDialog(waiters, selectedId) {
        const select = document.createElement('select');
        select.className = 'form-select mb-3';

        waiters.forEach(waiter => {
            if (waiter?.id && waiter?.name) {
                const option = document.createElement('option');
                option.value = waiter.id;
                option.textContent = waiter.name;
                option.selected = waiter.id === selectedId;
                select.appendChild(option);
            }
        });

        const container = document.createElement('div');
        container.appendChild(select);

        return this.dialog.confirm(container, {
            title: _t("Select Waiter"),
            confirm: _t("Assign"),
            cancel: _t("Cancel"),
        });
    },

    async _assignWaiterToOrder(waiter) {
        try {
            // Validate order and waiter exist
            if (!this.props.order || !waiter?.id) {
                throw new Error("Invalid order or waiter");
            }

            // Update frontend first
            this.props.order.set_waiter(waiter.id, waiter.name, waiter, true);

            // Robust RPC call with error handling
            const result = await this.rpc('/pos/assign_waiter', {
                order_id: this.props.order.id,
                waiter_id: waiter.id
            }, {
                timeout: 10000,
                shadow: true
            });

            if (!result.success) {
                throw new Error(result.error || "Failed to assign waiter");
            }

            this.notification.add(
                _t("Waiter %s assigned", waiter.name),
                { type: 'success' }
            );
        } catch (error) {
            console.error("Waiter assignment failed:", error);
            // Revert frontend changes if backend failed
            if (this.props.order) {
                this.props.order.set_waiter(null, null, null, false);
            }
            throw error;
        }
    }
});







