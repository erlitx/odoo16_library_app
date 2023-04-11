# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CrmExtend(models.Model):
    _inherit = 'crm.lead'
    description = fields.Text(string='Description_TEST')
    function = fields.Text(string='Function')
    product_id = fields.Many2one('product.product', string='Product to be sold')




# class crm_test(models.Model):
#     _name = 'crm_test.crm_test'
#     _description = 'crm_test.crm_test'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
