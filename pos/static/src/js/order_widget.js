/** @odoo-module **/
import { OrderWidget } from "@point_of_sale/app/generic_components/order_widget/order_widget";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";

patch(OrderWidget.prototype, {
    setup() {
        super.setup();
        this.dialog = useService("dialog");
        this.pos = useService("pos");
        this.notification = useService("notification");
        // Store selected waiter locally
        this._selectedWaiterId = null;
    },

    get waiter() {
        return this.props.order.get_waiter();
    },

  async onClickWaiterButton() {
    try {
        // Wait for POS to be fully loaded
        await this.pos.ready;

        // Debug: log all employee data
        Object.keys(this.pos.models['hr.employee'][0] || 'No employees loaded');
        const allEmployees = this.pos.models['hr.employee'];
        console.log("All employees data:", allEmployees.map(e => ({
            id: e.id,
            name: e.name,
            is_waiter:Boolean(e.is_waiter) || e.is_waiter
        })));

        // Filter only waiters
        const waiters = allEmployees.filter(e => e.is_waiter === true);

        if (!waiters.length) {
            this.notification.add(
                _t("No employees marked as waiters found. Please mark employees as waiters in the Employees app first."),
                {
                    type: 'warning',
                    title: _t("Waiter Setup Required"),
                    sticky: true  // Makes the notification stay until dismissed
                }
            );
            return;
        }

        // Set initial selected waiter (current waiter or first available)
        this._selectedWaiterId = this.waiter?.id || waiters[0]?.id;

        // Create dialog content
        const select = document.createElement('select');
        select.className = 'form-select mb-3';
        select.style.width = '100%';

        waiters.forEach(waiter => {
            const option = document.createElement('option');
            option.value = waiter.id;
            option.textContent = waiter.name;
            if (waiter.id === this._selectedWaiterId) {
                option.selected = true;
            }
            select.appendChild(option);
        });

        select.addEventListener('change', (ev) => {
            this._selectedWaiterId = parseInt(ev.target.value);
        });

        const container = document.createElement('div');
        container.appendChild(select);

        // Show confirmation dialog
        const confirmed = await this.dialog.confirm(container, {
            title: _t("Select Waiter"),
            confirm: _t("Assign Waiter"),
            cancel: _t("Cancel"),
        });

        // If confirmed and a waiter was selected
        if (confirmed && this._selectedWaiterId) {
            const selectedWaiter = waiters.find(w => w.id === this._selectedWaiterId);
            if (selectedWaiter) {
                this.props.order.set_waiter(selectedWaiter);
                this.notification.add(
                    _t("Waiter %s has been assigned to this order", selectedWaiter.name),
                    {
                        type: 'success',
                        title: _t("Waiter Assigned"),
                        sticky: false
                    }
                );
            }
        }
    } catch (error) {
        console.error("Waiter selection error:", error);
        this.notification.add(
            _t("An error occurred while selecting waiter. Please try again."),
            {
                type: 'danger',
                title: _t("Error"),
                sticky: true
            }
        );
        }
    },

    _createWaiterSelectionBody(waiters) {
        const select = document.createElement('select');
        select.className = 'form-select mb-3';
        select.style.width = '100%';

        waiters.forEach(waiter => {
            const option = document.createElement('option');
            option.value = waiter.id;
            option.textContent = waiter.name;
            if (waiter.id === this._selectedWaiterId) {
                option.selected = true;
            }
            select.appendChild(option);
        });

        select.addEventListener('change', (ev) => {
            this._selectedWaiterId = parseInt(ev.target.value);
        });

        const container = document.createElement('div');
        container.appendChild(select);
        return container;
    },
});