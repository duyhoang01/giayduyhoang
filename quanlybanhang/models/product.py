# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Product(models.Model):
    _name = 'product'

    code = fields.Char('Code')
    name = fields.Char('Name')
    meta_title = fields.Char('Meta Title')
    category = fields.Many2one('product.category', 'Product Category')
    provider = fields.Many2one('product.provider', 'Product Provider')

class Category(models.Model):
    _name = 'product.category'

    code = fields.Char('Code Category')
    name = fields.Char('Name Category')
    parent = fields.Many2one('product.category', string='Parent Category', index=True)

class Provider(models.Model):
    _name = 'product.provider'

    code = fields.Char('Code Provider')
    name = fields.Char('Name Provider')
    parent = fields.Many2one('product.provider', string='Parent Provider', index=True)