# -*- coding: utf-8 -*-


from odoo.exceptions import UserError, ValidationError
from odoo import models, fields, api, _
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)


class PosWaiter(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = 'pos.waiter'
    _description = 'POS Waiter'
    # endregion
    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------

    name = fields.Char('Waiter Name', required=True)
    active = fields.Boolean('Active', default=True)
    barcode = fields.Char('Barcode', help='Used for quick scanning')
    image = fields.Binary('Photo')



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

