# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class GroupProduct(models.Model):
    _name = 'group.product'
    _rec_name = 'name'

    name = fields.Char(string='Code', readonly=True, default=lambda self: _('New'))
    size = fields.Char(string='Size')
    color = fields.Char(string='Color')
    # size = fields.Selection([('size37','37'),
    #                          ('size38','38'),
    #                          ('size39','39'),
    #                          ('size40','40'),
    #                          ('size41','41'),
    #                          ('size42','42'),
    #                          ('size43','43'),
    #                          ('size44','44'),
    #                           ('size44','45')], string='Size')


    parent = fields.Many2one('group.product', string='Parent Group', index=True)

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('group.product.sequence') or _('New')
        return super(GroupProduct, self).create(vals)