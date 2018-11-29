# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrderDetail(models.Model):
    _name = 'sale.order.detail'

    order_id = fields.Many2one('sale.order', string='Order Reference', required=True, ondelete='cascade', index=True)
    grouppro_pro_id = fields.Many2one('group.product.detail', string="Group Product Detail")
    name = fields.Text(string='Description')
    sequence = fields.Integer(string='Sequence', default=1)
    quantity = fields.Integer(string='Quantity', default=1)
    tax = fields.Integer(string='Tax(%)', default=10)
    price_unit = fields.Float(string='Price Unit')

    color = fields.Char(string='Color', readonly=True, related='grouppro_pro_id.group_id.color')
    size = fields.Char(string='Size', readonly=True, related='grouppro_pro_id.group_id.size')

    price_subtotal = fields.Float(compute='_compute_amount', string='Subtotal', readonly=True, store=True)
    price_tax = fields.Float(compute='_compute_amount', string='Taxes', readonly=True, store=True)

    @api.depends('quantity', 'price_unit', 'tax')
    def _compute_amount(self):
        for line in self:
            price = line.quantity * line.price_unit
            taxes = price*line.tax/100
            line.update({
                'price_tax': taxes,
                'price_subtotal': price,
            })

    @api.onchange('grouppro_pro_id')
    def map_price_unit(self):
        self.price_unit = self.grouppro_pro_id.price_unit