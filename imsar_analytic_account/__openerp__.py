# -*- coding: utf-8 -*-
##############################################################################
#
#    IMSAR LLC
#    Author: IMSAR LLC
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
############################################################################################################################################################

{
    "name" : "IMSAR Customized Analytic Accounts",
    "version" : "1.0",
    "author" : "IMSAR LLC",
    "category": 'Uncategorized',
    'complexity': "normal",
    "description": """Analytic Account customizations.""",
    'website': 'http://www.imsar.com',
    "depends" : ['base', "account", "analytic", "account_analytic_analysis", "analytic_contract_hr_expense"],
    "data" : ['analytic_view.xml'],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
