# -*- coding: utf-8 -*-

from odoo import api, fields, models

class GroupProductDetail(models.Model):
    _name = 'group.product.detail'
    _rec_name = 'product_id'

    name = fields.Char(string='Group Product Detail')
    product_id = fields.Many2one('product', string='Product', required=True)
    group_id = fields.Many2one('group.product', string='Group Product', required=True)
    quantity = fields.Integer(string='Quantity')
    price_unit = fields.Float(string='Unit Price', digits=0)
    sequence = fields.Integer(string='Sequence', default=1)


