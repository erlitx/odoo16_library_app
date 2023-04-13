
# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CrmExtend(models.Model):
    _inherit = 'crm.lead'
    description = fields.Text(string='Description_TEST')
    function = fields.Text(string='Function')
    product_id = fields.Many2one('product.product', string='Product to be sold')
