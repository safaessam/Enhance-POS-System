from odoo import http, _
import logging
from odoo.http import request
import json
_logger = logging.getLogger(__name__)


class PosController(http.Controller):
    @http.route('/pos/assign_waiter', type='json', auth='user')
    def assign_waiter(self, order_id, waiter_id):
        """Secure waiter assignment endpoint"""
        try:
            result = request.env['pos.config'].assign_waiter(order_id, waiter_id)
            if not result['success']:
                _logger.warning("Waiter assignment failed: %s", result.get('error'))
            return result
        except Exception as e:
            _logger.error("Waiter assignment error: %s", str(e), exc_info=True)
            return {
                'success': False,
                'error': _("Server error occurred")
            }
# # -*- coding: utf-8 -*-
# from odoo import http
# from odoo.http import request
#
# class PosWaiterController(http.Controller):
#     @http.route('/pos/session/assign_waiter', type='json', auth='user')
#     def assign_waiter(self, session_id, order_id, waiter_id, **kwargs):
#         session = request.env['pos.session'].browse(session_id).exists()
#         if not session:
#             return {'error': 'Session not found'}
#         return session.assign_waiter_to_order(order_id, waiter_id)