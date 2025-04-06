import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { patch } from "@web/core/utils/patch";

    patch(PosOrder.prototype, {
     setup() {
        super.setup(...arguments);
        this.waiter_id = null;
        this.waiter_name = null;
        this.waiter_data = null;
        this.is_waiter = false;
        console.log("Setup completed with waiter_id:", this.waiter_id);
    },

    init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        console.log("Initializing from JSON:", json);
        this.set_waiter(
            json.waiter_id,
            json.waiter_name,
            json.waiter_data,
            json.is_waiter || false
        );
        console.log("Waiter set:", this.waiter_id, this.waiter_name, this.is_waiter);
    },

    export_as_JSON() {
        const json = super.export_as_JSON();
        console.log("Exporting as JSON:", json);
        return {
            ...json,
            waiter_id: this.waiter_id,
            waiter_name: this.waiter_name,
            waiter_data: this.waiter_data,
            is_waiter: this.is_waiter
        };
    },


    /**
     * Set waiter for the order with validation
     * @param {number} waiterId
     * @param {string} waiterName
     * @param {object} waiterData
     * @param {boolean} isWaiter
     */
    set_waiter(waiterId, waiterName, waiterData = null, isWaiter = true) {
        if (this.waiter_id === waiterId &&
            this.waiter_name === waiterName &&
            this.is_waiter === isWaiter) {
            return;
        }

        // Validate inputs
        if (!waiterId || !waiterName) {
            throw new Error("Invalid waiter information provided");
        }

        this.waiter_id = waiterId;
        this.waiter_name = waiterName;
        this.waiter_data = waiterData || {
            id: waiterId,
            name: waiterName,
            is_waiter: isWaiter
        };
        this.is_waiter = isWaiter;

        this.trigger('change', this);
        this.trigger('change-waiter', {
            order: this,
            waiter: this.waiter_data
        });
    },

    // Enhanced waiter assignment in component
    async assignWaiter(waiter) {
        try {
            if (!this.props.order || !waiter?.id) {
                throw new Error("Invalid order or waiter");
            }

            // Update frontend first
            this.props.order.set_waiter(
                waiter.id,
                waiter.name,
                waiter,
                true
            );

            // Sync with backend
            await this.orm.call(
                'pos.order',
                'write',
                [[this.props.order.id], {
                    waiter_id: waiter.id,
                    waiter_name: waiter.name,
                    is_waiter: true

                }],
                { shadow: true }  // Optional: mark as shadow request
            );

            // Show success notification
            this.notification.add(
                _t("Waiter %s assigned", waiter.name),
                { type: 'success' }
            );

            return true;
        } catch (error) {
            console.error("Waiter assignment failed:", error);

            // Revert frontend changes if backend failed
            if (this.props.order) {
                this.props.order.set_waiter(null, null, null, false);
            }

            this.notification.add(
                _t("Failed to assign waiter"),
                { type: 'danger' }
            );

            throw error;
        }
    }
});
    /**
     * Set waiter for the order
     * @param {number|null} waiterId
     * @param {string|null} waiterName
     * @param {object|null} waiterData
     * @param {boolean} [isWaiter=false]
     */
//    set_waiter(waiterId, waiterName, waiterData = null, isWaiter = false) {
//        const newIsWaiter = Boolean(isWaiter);
//        const changed = (
//            this.waiter_id !== waiterId ||
//            this.waiter_name !== waiterName ||
//            this.is_waiter !== newIsWaiter
//        );
//
//        if (!changed) return;
//
//        this.waiter_id = waiterId || null;
//        this.waiter_name = waiterName || null;
//        this.waiter_data = waiterData || null;
//        this.is_waiter = newIsWaiter;
//
//        this.trigger('change', this);
//        this.trigger('change-waiter', {
//            order: this,
//            waiter: this.waiter_data,
//            is_waiter: newIsWaiter
//        });
//    },
//
//    /**
//     * Get current waiter information
//     * @returns {object|null} Waiter data
//     */
//    get_waiter() {
//        return this.waiter_data || {
//            id: this.waiter_id,
//            name: this.waiter_name,
////            is_waiter: this.is_waiter
//        };
//    },
//
//    /**
//     * Check if order has a waiter assigned
//     * @returns {boolean}
//     */
//    has_waiter() {
//        return Boolean(this.waiter_id) && this.is_waiter;
//    },
//
//    get_orderlines() {
//        return this.lines || [];
//    },
//
//    get_payments() {
//        return this.payment_ids || [];
//    },
//
//    get_pos_orders() {
//        return this.pos_orders || [];
//    },
//
//    /**
//     * Clear waiter assignment
//     */
//    clear_waiter() {
//        this.set_waiter(null, null, null, false);
//    },
//
//    /**
//     * Check if the assigned staff is specifically a waiter
//     * @returns {boolean}
//     */
//    is_specific_waiter() {
//        return this.is_waiter;
//    }
//});

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
