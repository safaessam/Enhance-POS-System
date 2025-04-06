# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

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
        readonly=True,
        help='Employee responsible for this order',
        domain=[('is_waiter', '=', True)],)
    # waiter_ids = fields.Many2many('hr.employee', string="Waiters",domain=[('is_waiter', '=', 'True')])
    # region  Basic
    # endregion

    # Load POS data fields

    @api.model
    def _load_pos_data_fields(self, config_id):
        fields = super()._load_pos_data_fields(config_id)
        fields += ['partner_id', 'table_id', 'lines']  # Include lines
        if self.env['pos.config'].browse(config_id).module_pos_restaurant:
            fields += ['waiter_id']
        return fields

    def _export_for_ui(self, order):
        result = super()._export_for_ui(order)
        result.update({
            'partner_id': order.partner_id.id if order.partner_id else False,
            'table_id': order.table_id.id if order.table_id else False,
            'lines': order.lines.ids if order.lines else [],
            'waiter_id': order.waiter_id.id if order.waiter_id else False,
            'waiter_name': order.waiter_id.name if order.waiter_id else False
        })
        return result

    def _order_fields(self, ui_order):
        order_fields = super()._order_fields(ui_order)
        order_fields.update({
            'partner_id': ui_order.get('partner_id', False),
            'table_id': ui_order.get('table_id', False),
            'lines': ui_order.get('lines', []),
            'waiter_id': ui_order.get('waiter_id', False)
        })
        return order_fields


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
    @api.constrains('waiter_id')
    def _check_waiter(self):
        for order in self:
            if not order.waiter_id:
                raise ValidationError("You must assign a waiter to the order before proceeding.")

    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------



    # endregion
