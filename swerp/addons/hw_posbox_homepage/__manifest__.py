# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

{
    'name': 'IoT Box Homepage',
    'category': 'Sales/Point Of Sale',
    'sequence': 6,
    'website': 'https://www.swerp.it/page/point-of-sale-hardware',
    'summary': 'A homepage for the IoT Box',
    'description': """
IoT Box Homepage
================

This module overrides Swerp web interface to display a simple
Homepage that explains what's the iotbox and shows the status,
and where to find documentation.

If you activate this module, you won't be able to access the 
regular Swerp interface anymore.

""",
    'depends': ['hw_proxy'],
    'installable': False,
}
