# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class PosSession(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _inherit = 'pos.session'
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    # endregion

    # region  Special
    # endregion

    # region  Relational
    # endregion

    # region  Computed
    # endregion

    # endregion
    # region ---------------------- TODO[IMP]: Compute methods ------------------------------------



    @api.model
    def _load_pos_data_models(self, config_id):
        data = super()._load_pos_data_models(config_id)
        data += ['hr.employee']  # Load employee data for waiter functionality
        return data

    # Method to assign waiter to a specific order
    @api.model
    def assign_waiter(self, order_id, waiter_id):
        order = self.env['pos.order'].browse(order_id)
        if not order:
            raise UserError('Order not found!')
        if not self.env['hr.employee'].browse(waiter_id):
            raise ValidationError('Invalid waiter!')
        order.waiter_id = waiter_id

    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------

    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------



    # endregion
