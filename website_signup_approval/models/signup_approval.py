# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Vishnu KP @ Cybrosys, (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import fields, models


class SignupApproval(models.Model):
    """Store Information's of User"""
    _name = 'signup.approval'
    _description = "Approval Request Details"

    login = fields.Char(string='Email', help="Login details of user")
    name = fields.Char(string='Name', help="Name of the user")
    approved_date = fields.Datetime(string='Approved Date', copy=False,
                                    help="Approval date of signup request")
    for_approval_menu = fields.Boolean(string='For Approval Menu',
                                       help="Check the request is approved")

    def action_approve_login(self):
        """To approve the request from website"""
        self.env['res.users'].create({
            'name': self.name,
            'login': self.login,
        })
        self.env.ref('base.group_user').users.ids.pop()
