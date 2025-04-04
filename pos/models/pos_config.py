# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class PosConfig(models.Model):    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _inherit = 'pos.config'    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    require_waiter = fields.Boolean('Require Waiter Assignment', default=True)
    default_waiter = fields.Many2one('pos.waiter', string='Default Waiter')

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
