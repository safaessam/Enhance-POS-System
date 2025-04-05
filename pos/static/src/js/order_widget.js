/** @odoo-module **/
import { OrderWidget } from "@point_of_sale/app/generic_components/order_widget/order_widget";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { useState } from "@odoo/owl";
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";
patch(OrderWidget.prototype, {
        setup() {
            super.setup();
            this.pos = useService("pos");
            this.dialog = useService("dialog");
            this.notification = useService("notification");

            // Bind selectWaiter method to the context
            this.selectWaiter = this.selectWaiter.bind(this);

            this.state = useState({
                hasOrder: false,
                isLoading: false,
                waiter: null,
            });
        },

        onMounted() {
            super.onMounted?.();
            this._updateOrderState();
        },

        onWillUpdateProps() {
            super.onWillUpdateProps?.();
            this._updateOrderState();
        },

        _updateOrderState() {
            const order = this.pos.get_order();
            this.state.hasOrder = !!order && !!order.get_orderlines;
            if (this.state.hasOrder) {
                this.state.waiter = order.waiter_id
                    ? this.pos.employees.find(e => e.id === order.waiter_id)
                    : null;
            }
        },

        async selectWaiter() {
            if (!this.state.hasOrder || this.state.isLoading) return;

            try {
                this.state.isLoading = true;
                const order = this.pos.get_order();

                if (!this.pos.config.module_pos_restaurant) return;

                const waiters = this.pos.employees.filter(emp => emp.is_waiter);
                if (!waiters.length) {
                    this.notification.add(this.env._t("No waiters available"), 3000);
                    return;
                }

                const { confirmed, payload: selectedWaiter } = await this.dialog.add(SelectionPopup, {
                    title: this.env._t("Select Waiter"),
                    list: waiters.map(waiter => ({
                        id: waiter.id,
                        item: waiter,
                        label: waiter.name || this.env._t("Unnamed"),
                        isSelected: order.waiter_id === waiter.id,
                    })),
                    search: true,
                });

                if (confirmed) {
                    if (!selectedWaiter) {
                        this.notification.add(this.env._t("A waiter must be selected to proceed"), 3000);
                        return;
                    }
                    order.set_waiter(selectedWaiter);
                    this.state.waiter = selectedWaiter;
                }
            } catch (error) {
                console.error("Waiter selection error:", error);
                this.notification.add(this.env._t("Error assigning waiter"), 3000);
            } finally {
                this.state.isLoading = false;
            }
        },
    });

