# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.


{
    'name': 'Contacts',
    'category': 'Tools',
    'summary': 'Centralize your address book',
    'description': """
This module gives you a quick view of your contacts directory, accessible from your home page.
You can track your vendors, customers and other contacts.
""",
    'depends': ['base', 'mail'],
    'data': [
        'views/contact_views.xml',
    ],
    'application': True,
}
