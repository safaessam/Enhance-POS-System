# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class PosSession(models.Model):
    _inherit = 'pos.session'


    is_waiter = fields.Boolean(
        string='Is Waiter',
        default=True,
        help='Check this box if this employee is a waiter in the restaurant'
    )

    @api.model
    def _load_pos_data_models(self, config_id):
        models = super()._load_pos_data_models(config_id)
        models += ['hr.employee']
        return models

    @api.model
    def _load_pos_data_fields(self, config_id):
        fields = super()._load_pos_data_fields(config_id)
        fields.append('is_waiter')  # Add 'is_waiter' field here
        return fields

    def get_waiter_employees(self):
        # Filter employees where 'is_waiter' is True
        waiter_employees = self.env['hr.employee'].search([('is_waiter', '=', True)])
        return waiter_employees
    # ---------------------- Fields Declaration --------------------------------
    # is_waiter = fields.Boolean(
    #     string='Is Waiter',
    #     default=False,
    #     help='Check this box if this employee is a waiter in the restaurant'
    # )
    #
    # # ---------------------- Load POS Data Methods ----------------------------
    # @api.model
    # def _load_pos_data_models(self, config_id):
    #     data = super()._load_pos_data_models(config_id)
    #     data.append('hr.employee')  # Load employee data for waiter functionality
    #     return data
    #
    # def _loader_params_hr_employee(self):
    #     return {
    #         'search_params': {
    #             'domain': [('is_waiter', '=', True)],  # Only load waiters
    #             'fields': ['name', 'id', 'is_waiter'],
    #         }
    #     }
    #
    # # ---------------------- Waiter Assignment Methods ------------------------
    # def assign_waiter_to_order(self, order_id, waiter_id):
    #     """Assign waiter to POS order with validation"""
    #     order = self.env['pos.order'].browse(order_id)
    #     if not order.exists():
    #         raise ValueError("Order not found")
    #
    #     waiter = self.env['hr.employee'].browse(waiter_id)
    #     if not waiter.exists() or not waiter.is_waiter:
    #         raise ValueError("Invalid waiter selection")
    #
    #     order.write({'waiter_id': waiter_id})
    #     return {
    #         'success': True,
    #         'waiter_name': waiter.name
    #     }
    #
    # # ---------------------- Order Processing Methods -------------------------
    # def _process_order(self, order, draft):
    #     """Override to handle missing session_id"""
    #     if 'session_id' not in order:
    #         # Try to get session from context
    #         session_id = self.env.context.get('active_id')
    #         if not session_id:
    #             # Get latest open session for current user
    #             session = self.env['pos.session'].search([
    #                 ('state', '=', 'opened'),
    #                 ('user_id', '=', self.env.uid),
    #             ], limit=1)
    #             if not session:
    #                 raise UserError("No active POS session found. Please open a session first.")
    #             session_id = session.id
    #         order['session_id'] = session_id
    #
    #     # Call original _process_order
    #     return super(PosSession, self)._process_order(order, draft)


