# -*- coding: utf-8 -*-
{
    'name': 'Invoice Multi Currency',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Show invoice amounts in both invoice currency and company currency',
    'description': """
Invoice Multi Currency
========================

Display invoice total amounts in both the invoice currency and the company currency
on invoice and bill form views and list views.

Main Features
-------------
* Show untaxed, tax, total, and amount due in company currency on the invoice form.
* Company currency amounts appear only when the invoice currency differs from the company currency.
* Additional company currency total column on invoice and bill list views.
* No new models or fields — uses existing Odoo 18 computed fields.
    """,
    'author': 'Steven Marp',
    'website': 'https://apps.odoo.com/apps/modules/browse?author=Steven Marp',
    'license': 'LGPL-3',
    'depends': ['account'],
    'data': [
        'views/account_move_views.xml',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
    'price': 29.22,
    'currency': 'USD',
}
