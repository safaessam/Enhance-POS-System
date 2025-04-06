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