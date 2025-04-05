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
        help='Check this box if this employee is a waiter in the restaurant'
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

    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------
    @api.model
    def _load_pos_data_fields(self, config_id):
        data = super()._load_pos_data_fields(config_id)
        data += ['is_waiter']
        return data

# return ['id', 'name','is_waiter']


        # return ['id', 'name','is_waiter']

    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    # endregion
class ResUsers(models.Model):

    _inherit = 'res.users'


    hide_product_information = fields.Boolean()


    @api.model

    def _load_pos_data_fields(self, config_id):

        res = super()._load_pos_data_fields(config_id)

        res += ['hide_product_information']

        return res


