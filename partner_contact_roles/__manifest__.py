# -*- coding: utf-8 -*-
{
    'name': 'Partner Contact Roles',
    'version': '18.0.1.1.0',
    'category': 'Sales/CRM',
    'summary': 'Adds simple "Is a Customer" and "Is a Vendor" checkboxes to the contact form.',
    'description': """
This module provides a user-friendly way to classify contacts as customers or vendors
using simple boolean checkboxes. The checkboxes are synchronized with Odoo's standard
customer_rank and supplier_rank fields for seamless integration.
    """,
    'author': 'Techbot ERP',
    'website': 'https://techboterp.com',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'sale_management',
        'purchase',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
    # Add an icon for your module (optional). Create a file named 'icon.png'
    # in the 'static/description/' directory.
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}