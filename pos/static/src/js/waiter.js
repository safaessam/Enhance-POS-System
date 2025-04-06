//// static/src/js/WaiterSelection.js
///** @odoo-module **/
//
//import { usePos } from "@point_of_sale/app/store/pos_hook";
//import { patch } from "@web/core/utils/patch";
//import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";
//import { _t } from "@web/core/l10n/translation";
//import { ActionpadWidget } from "@point_of_sale/app/screens/product_screen/action_pad/action_pad";
//
//patch(ActionpadWidget.prototype, {
//    setup() {
//        super.setup();
//        this.pos = usePos();
//    },
//    async selectWaiter() {
//        if (!this.pos.config.module_pos_restaurant) {
//            return;
//        }
//
//        // Get waiters from employees (filtered by is_waiter flag)
//        const waiters = this.pos.employees.filter(employee =>
//            employee.is_waiter
//        );
//
//        if (waiters.length === 0) {
//            this.pos.notification.add(_t("No waiters available"), 3000);
//            return;
//        }
//
//        const { confirmed, payload: selectedWaiter } = await this.pos.popup.add(SelectionPopup, {
//            title: _t("Select Waiter"),
//            list: waiters.map(waiter => ({
//                id: waiter.id,
//                item: waiter,
//                label: waiter.name,
//            })),
//        });
//
//        if (confirmed) {
//            this.pos.get_order().set_waiter(selectedWaiter);
//        }
//    },
//});