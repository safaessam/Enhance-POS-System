# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging


_logger = logging.getLogger(__name__)

class PosOrder(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = 'pos.order'
    _inherit = ['pos.order', 'pos.load.mixin']    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    waiter_id = fields.Many2one(
        'hr.employee',
        string='Assigned Waiter',
        domain=[('is_waiter', '=', True)],
        help='Employee responsible for this order'
    )

    # Load POS data fields
    @api.model
    def _process_order(self, order, existing_order=None):
        """Enhanced order processing with validation"""
        try:
            # Convert orders to list if a single order is passed
            if isinstance(order, dict):
                order = [order]

            # Validate input (ensure it's a list of orders)
            if not isinstance(order, list):
                raise ValidationError(_("Orders must be a list"))

            order_ids = []  # List to hold order IDs
            for o in order:  # Loop through orders
                if not isinstance(o, dict):
                    raise ValidationError(_("Each order must be a dictionary"))

                draft = True if o.get('state') == 'draft' else False
                # You can continue processing the order here, e.g. creating or updating records
                order_ids.append(self.create(o))  # This is just an example. Adjust based on your logic.

            return order_ids
        except Exception as e:
            _logger.error("Order processing failed: %s", str(e), exc_info=True)
            raise

    @api.model
    def _order_fields(self, ui_order):
        """Handle order fields with validation"""
        fields = super(PosOrder, self)._order_fields(ui_order)

        # Safely add waiter fields
        if isinstance(ui_order, dict):
            fields.update({
                'waiter_id': ui_order.get('waiter_id'),
                'waiter_name': ui_order.get('waiter_name'),
                'waiter_data': ui_order.get('waiter_data', {})
            })
        return fields


    # @api.model
    # def sync_from_ui(self, orders):
    #     """
    #     Robust order synchronization with proper error handling
    #     """
    #     try:
    #         if not isinstance(orders, list):
    #             _logger.error("Invalid orders format: %s", type(orders))
    #             return {
    #                 'success': False,
    #                 'error': _("Invalid orders format"),
    #                 'code': 'INVALID_FORMAT'
    #             }
    #
    #         results = []
    #         for order in orders:
    #             try:
    #                 # Validate required fields
    #                 if not all(k in order for k in ['id', 'lines', 'config_id']):
    #                     raise UserError(_("Missing required order fields"))
    #
    #                 # Process with parent implementation
    #                 order_id = super(PosOrder, self)._process_order(
    #                     order,
    #                     draft=False,
    #                     existing_order=order.get('id', False)
    #                 )
    #                 results.append(order_id)
    #             except Exception as e:
    #                 _logger.error("Order processing failed: %s", str(e), exc_info=True)
    #                 results.append({
    #                     'success': False,
    #                     'error': str(e),
    #                     'order': order.get('id', 'unknown')
    #                 })
    #
    #         return {
    #             'success': True,
    #             'processed': len([r for r in results if isinstance(r, int)]),
    #             'failed': len([r for r in results if not isinstance(r, int)]),
    #             'results': results
    #         }
    #
    #     except Exception as e:
    #         _logger.error("Sync failed: %s", str(e), exc_info=True)
    #         return {
    #             'success': False,
    #             'error': _("Server error occurred"),
    #             'code': 'SERVER_ERROR'
    #         }

    @api.constrains('waiter_id')
    def _check_waiter_assignment(self):
        """Validate waiter assignment for restaurant orders"""
        for order in self:
            if order.config_id.module_pos_restaurant and not order.waiter_id:
                raise ValidationError("Waiter assignment is required for restaurant orders")
    # endregion

    # region  Computed
    # endregion

    # endregion
    # region ---------------------- TODO[IMP]: Compute methods ------------------------------------

    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------
    #


    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------



    # endregion
