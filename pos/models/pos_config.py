# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class PosConfig(models.Model):    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _inherit = 'pos.config'    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    available_waiters = fields.Many2many('res.users', string='Available Waiters')
    require_waiter = fields.Boolean('Require Waiter Assignment', default=True)
    default_waiter = fields.Many2one('res.users', string='Default Waiter', domain=[('is_waiter', '=', True)])
    employee_ids = fields.Many2many('hr.employee', 'pos_config_employee_rel', 'pos_config_id', 'employee_id', string='Employees')
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
    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------
    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    # endregion
