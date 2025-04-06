# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class HrEmployee(models.Model):
    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _inherit = ['hr.employee']    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------

    is_waiter = fields.Boolean(
        string='Is Waiter',
        default=False,
        # store=True,
        help='Check this box if this employee is a waiter in the restaurant',
        # groups="base.group_user"
    )
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
    # Make sure that `is_waiter` is included in the returned fields

    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------
    # @api.model
    # def _load_pos_data_fields(self, config_id):
    #     """Override to include waiter fields in POS data loading"""
    #     fields = super()._load_pos_data_fields(config_id)
    #     fields.append('is_waiter')
    #     return fields

    @api.model
    def _load_pos_data_fields(self, config_id):
        fields = super()._load_pos_data_fields(config_id)
        return fields + ['is_waiter']





    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    # endregion

