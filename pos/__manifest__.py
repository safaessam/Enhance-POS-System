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
    'depends': ['point_of_sale' ,'mail', 'base','hr'],
    'data': [
        # 'views/pos_config_views.xml',
        # 'views/pos_order_views.xml',
        # # 'views/pos_template.xml',
        # 'views/res_users_views.xml',
    ],
    # 'assets': {
    #     'point_of_sale.assets': [
    #         'pos/static/src/js/waiter.js',
    #         # 'pos/static/src/js/pos.js',
    #         'pos/static/src/xml/**/*',
    #
    #     ],
    # },
        "assets": {
            "point_of_sale._assets_pos": [
                "pos/static/src/xml/waiter.xml",
                "pos/static/src/js/waiter.js",
        ]
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
