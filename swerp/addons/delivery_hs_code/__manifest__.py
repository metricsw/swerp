# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.


{
    'name': 'Delivery HS Code',
    'version': '1.0',
    'category': 'Stock',
    'description': """
Set back field hs_code on pruduct template.
==============================================================

""",
    'depends': ['delivery'],
    'data': [
        'views/product_template_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}
