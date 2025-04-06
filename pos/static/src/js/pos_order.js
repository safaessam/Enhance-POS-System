
import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { patch } from "@web/core/utils/patch";

patch(PosOrder.prototype, {
    setup() {
        super.setup(...arguments);
        this.waiter_id = this.waiter_id || null;
        this.waiter_name = this.waiter_name || null;
        this.waiter_data = this.waiter_data || null;
        this.is_waiter = this.is_waiter || false;  // Default to false if undefined
        this.lines = this.lines || [];
        this.payment_ids = this.payment_ids || [];
    },

    init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        this.set_waiter(
            json.waiter_id || null,
            json.waiter_name || null,
            json.waiter_data || null,
            json.is_waiter || false  // Default to false if undefined
        );
        this.lines = json.lines || [];
        this.payment_ids = json.payment_ids || [];
    },

    export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        return {
            ...json,
            waiter_id: this.waiter_id,
            waiter_name: this.waiter_name,
            waiter_data: this.waiter_data,
            is_waiter: this.is_waiter || false,  // Ensure boolean value
            lines: this.lines,
            payment_ids: this.payment_ids
        };
    },

    /**
     * Set waiter for the order
     * @param {number|null} waiterId
     * @param {string|null} waiterName
     * @param {object|null} waiterData
     * @param {boolean} [isWaiter=false]
     */
    set_waiter(waiterId, waiterName, waiterData = null, isWaiter = false) {
        // Convert undefined to false
        const actualIsWaiter = typeof isWaiter === 'undefined' ? false : Boolean(isWaiter);

        const changed = this.waiter_id !== waiterId || this.is_waiter !== actualIsWaiter;
        this.waiter_id = waiterId || null;
        this.waiter_name = waiterName || null;
        this.waiter_data = waiterData || null;
        this.is_waiter = actualIsWaiter;

        if (changed) {
            this.trigger('change', this);
            this.trigger('change-waiter', {
                order: this,
                waiter: waiterData,
                is_waiter: actualIsWaiter
            });
        }
    },

    /**
     * Get current waiter information
     * @returns {object|null} Waiter data
     */
    get_waiter() {
        return this.waiter_data || {
            id: this.waiter_id,
            name: this.waiter_name,
            is_waiter: this.is_waiter
        };
    },

    /**
     * Check if order has a waiter assigned
     * @returns {boolean}
     */
    has_waiter() {
        return this.is_waiter && Boolean(this.waiter_id);
    },

    get_orderlines() {
        return this.lines || [];
    },

    /**
     * Clear waiter assignment
     */
    clear_waiter() {
        this.set_waiter(null, null, null, false);
    },

    /**
     * Check if the assigned staff is specifically a waiter (not just any staff)
     * @returns {boolean}
     */
    is_specific_waiter() {
        return this.is_waiter;
    }
});

///** @odoo-module **/
//
//import { PosOrder } from "@point_of_sale/app/models/pos_order";
//import { patch } from "@web/core/utils/patch";
//
//patch(PosOrder.prototype, {
//    setup() {
//        super.setup(...arguments);
//        // Initialize all required fields with defaults
//        this.waiter_id = this.waiter_id || false;
//        this.waiter_name = this.waiter_name || false;
//        this.partner_id = this.partner_id || false;
//        this.table_id = this.table_id || false;
//    },
//
//    init_from_JSON(json) {
//        super.init_from_JSON(...arguments);
//        // Initialize all fields from JSON data
//        this.set_waiter(json.waiter_id || false, json.waiter_name || false);
//        this.partner_id = json.partner_id || false;
//        this.table_id = json.table_id || false;
//    },
//
//    export_as_JSON() {
//        const json = super.export_as_JSON(...arguments);
//        // Include all required fields in export
//        return {
//            ...json,
//            waiter_id: this.waiter_id || false,
//            waiter_name: this.waiter_name || false,
//            partner_id: this.partner_id || false,
//            table_id: this.table_id || false,
//        };
//    },
//
//    set_waiter(waiterId, waiterName) {
//        this.waiter_id = waiterId || false;
//        this.waiter_name = waiterName || false;
//        if (this.waiter_id) {
//            this.trigger('change', this);
//        }
//    },
//
//    get_waiter() {
//        if (!this.waiter_id) return null;
//        return {
//            id: this.waiter_id,
//            name: this.waiter_name,
//            employee: this.pos.employees.find(emp => emp.id === this.waiter_id) || null
//        };
//    },
//});
