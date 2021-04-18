# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Swerp Settings Dashboard',
    'version': '1.0',
    'summary': 'Quick actions for installing new app, adding users, etc.',
    'category': 'Extra Tools',
    'description':
    "Swerp dashboard ============== * Quick access to install apps * Quick users add * Quick access to the `App Store` and `Theme Store` ",
    'data': [
        'views/dashboard_views.xml',
        'views/dashboard_templates.xml',
    ],
    'depends': ['web'],
    'qweb': ['static/src/xml/dashboard.xml'],
    'auto_install': True,
}
