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
    },

    get waiter() {
        return this.props.order.get_waiter();
    },

    async onClickWaiterButton() {
    try {
        if (!this.pos || !this.pos.employees) {
            this.notification.add(
                _t("Employees data is not loaded yet"),
                { type: 'warning', title: _t("Waiter Assignment") }
            );
            return;
        }

        const waiterList = this.pos.employees.filter(
            employee => employee.is_waiter
        )
            .map(employee => ({
                id: employee.id,
                name: employee.name,
            }));

        if (!waiterList.length) {
            this.notification.add(
                _t("No waiters configured in the system"),
                { type: 'warning', title: _t("Waiter Assignment") }
            );
            return;
        }

        // Use standard dialog.confirm with custom body
        const confirmed = await this.dialog.confirm(
            this._createWaiterSelectionBody(waiterList),
            {
                title: _t("Select Waiter"),
                confirm: _t("Assign"),
                cancel: _t("Cancel"),
            }
        );

        if (confirmed) {
            const selectedId = parseInt(this._selectedWaiterId);
            const selectedWaiter = waiterList.find(w => w.id === selectedId);
            if (selectedWaiter) {
                this.props.order.set_waiter(selectedWaiter);
                this.notification.add(
                    _t("Waiter %s assigned", selectedWaiter.name),
                    { type: 'success', title: _t("Waiter Updated") }
                );
            }
        }
    } catch (error) {
        console.error("Waiter selection error:", error);
        this.notification.add(
            _t("Failed to select waiter. Please try again."),
            { type: 'danger', title: _t("Error") }
        );
    }

    },

    _createWaiterSelectionBody(waiters) {
        this._selectedWaiterId = this.waiter?.id || waiters[0]?.id;

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