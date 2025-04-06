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



    # @api.model
    # def _load_pos_data_models(self, config_id):
    #     data = super()._load_pos_data_models(config_id)
    #     data += ['hr.employee']  # Load employee data for waiter functionality
    #     return data

    @api.model
    def _load_pos_data_models(self, config_id):
        data = super()._load_pos_data_models(config_id)
        data.append('hr.employee')  # Load employee data for waiter functionality
        return data

    def _loader_params_hr_employee(self):
        return {
            'search_params': {
                'domain': [('is_waiter', '=', True)],  # Only load waiters
                'fields': ['name', 'id', 'is_waiter'],
            }
        }
    # Method to assign waiter to a specific order

    def assign_waiter_to_order(self, order_id, waiter_id):
        """Assign waiter to POS order with validation"""
        order = self.env['pos.order'].browse(order_id)
        if not order.exists():
            raise ValueError("Order not found")

        waiter = self.env['hr.employee'].browse(waiter_id)
        if not waiter.exists() or not waiter.is_waiter:
            raise ValueError("Invalid waiter selection")

        order.write({'waiter_id': waiter_id})
        return {
            'success': True,
            'waiter_name': waiter.name
        }
    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------

    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------



    # endregion
