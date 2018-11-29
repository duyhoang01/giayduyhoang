# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _name = 'qlbh.users'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code', readonly=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Char(string='address')
    sex = fields.Selection([('name','Nam'),('nu','Nữ')], string='Sex')
    position = fields.Selection([('cus','Customer'),('emp','Employee'),
                              ('man','Manager')], string='Position')