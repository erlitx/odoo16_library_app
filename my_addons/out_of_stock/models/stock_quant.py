# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductOutofstock(models.Model):
    # _name = 'products.outofstock'
    # _description = 'Out of stock products'
    _inherit = 'stock.quant'

    out_of_stock = fields.Integer(string="Out of Stock")

