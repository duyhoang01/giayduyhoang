# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _name = 'sale.order'

    name = fields.Char(string='Code', readonly=True, default=lambda self: _('New'))
    customer_id = fields.Many2one('qlbh.users', string='Customer')
    date_order = fields.Date(string='Date Order', readonly=True)
    sequence = fields.Integer(string='Sequence', default=1, readonly=True)
    order_detail = fields.One2many('sale.order.detail', 'order_id', string='Order Detail', auto_join=True)

    amount_untaxed = fields.Float(string='Untaxed Amount', store=True, readonly=True, compute='_amount_all')
    amount_tax = fields.Float(string='Taxes', store=True, readonly=True, compute='_amount_all')
    amount_total = fields.Float(string='Total', store=True, readonly=True, compute='_amount_all')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('sale.order.sequence') or _('New')
        vals['date_order'] = datetime.now().strftime('%m/%d/%Y')
        return super(SaleOrder, self).create(vals)

    @api.depends('order_detail.price_subtotal')
    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_detail:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax,
            })
