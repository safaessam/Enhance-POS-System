/**@odoo-module **/

import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

import { _t } from "@web/core/l10n/translation";

import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";

import { patch } from "@web/core/utils/patch";

patch(ControlButtons.prototype, {

    async onClickPopup() {

        this.dialog.add(AlertDialog, {

            title: _t("Custom Alert"),

            body: _t("Choose the alert type"),

        });

    },

});


