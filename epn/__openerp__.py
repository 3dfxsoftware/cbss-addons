# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'EPN Payment Processing',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Make credit card payments in the POS with the EPN network',
    'description': """
This modules allows you to integrate the epn credit-card processing network with
The point of sale. The EPN module needs an iPad application to process the payment.
This modules handles the communication between the iPad application and the Point of Sale.

""",
    'author': 'OpenERP SA',
    'depends': ['point_of_sale'],
    'data': [
        'views/templates.xml',
        'epn_view.xml',
    ],
    'js': [
        'static/src/js/phonegap.js',
        'static/src/js/main.js',
    ],
    'qweb':[
        'static/src/xml/epn.xml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
