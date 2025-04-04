# -*- coding: utf-8 -*-
{
    'name': 'POS Waiter Assignment',
    'version': "1.0.0",
    'summary': 'Assign waiters to POS orders and display on receipts',
    'description': """
       This module enhances the POS system by:
        - Adding waiter assignment functionality
        - Making waiter selection mandatory
        - Displaying waiter information on receipts
        - Tracking orders by waiter
    """,
    'author': 'Safa Essam',
    'category': 'Point of Sale',
    'depends': ['point_of_sale' ,'mail', 'base'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/pos_waiter_views.xml',
        # 'views/pos_config_views.xml',
        # 'views/pos_order_views.xml',
        # 'views/receipt_templates.xml',
        'views/menu.xml'


    ],
    'assets': {
        'point_of_sale.assets': [
            # 'pos/static/src/js/**/*',
        ],
        'web.assets_qweb': [
            # 'pos/static/src/xml/**/*',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
