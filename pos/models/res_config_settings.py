# -*- coding: utf-8 -*-


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class ResConfigSettings(models.TransientModel):
    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _inherit = 'res.config.settings'
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    pos_require_waiter = fields.Boolean(related='pos_config_id.require_waiter', readonly=False)
    pos_default_waiter = fields.Many2one(related='pos_config_id.default_waiter', readonly=False)

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
