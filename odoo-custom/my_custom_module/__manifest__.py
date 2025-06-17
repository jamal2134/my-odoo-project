# -*- coding: utf-8 -*-
{
    'name': 'Purchase Order API Hook',
    'version': '1.0.0',
    'summary': 'Send API call when a purchase order is confirmed',
    'description': """
        This module sends an HTTP API request to an external system
        whenever a purchase order is confirmed in Odoo.
    """,
    'author': 'Your Name or Company',
    'website': 'https://yourcompany.com',
    'category': 'Purchases',
    'depends': ['purchase'],
    'data': [
        # You can add XML/CSV files here like views, security, etc.
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
