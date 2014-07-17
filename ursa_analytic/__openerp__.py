# -*- coding: utf-8 -*-
##############################################################################
#
#    Ursa Information Systems
#    Author: Balaji Kannan
#    Copyright (C) 2014 (<http://www.ursainfosystems.com>).
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
    "name" : "Project Contract Customizations",
    "version" : "1.0",
    "author" : ["Ursa Information Systems, USA"],
    "category": 'Project',
    'complexity': "normal",
    "description": """
    1. Shows additional buttons on contract form
    2. Adds contract field to po, si, ci, is, do and integrates data
    """,
    'website': 'http://www.ursainfosystems.com',
    "depends" : ['analytic','sale','purchase','stock','account',],
    'init_xml': [],
    'update_xml': ['analytic_view.xml'],
    'demo_xml': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
