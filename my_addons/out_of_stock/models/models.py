# -*- coding: utf-8 -*-

# from odoo import models, fields, api
#
#
# class ProductOutofstock(models.Model):
#     # _name = 'products.outofstock'
#     # _description = 'Out of stock products'
#     _inherit = 'product.template'
#
#     some_description = fields.Char()
#    # qoh_location1 = fields.Float(string="QoH", store=True)
#    #  stock_quant_ids = fields.One2many('stock.quant', 'product_tmpl_id')  # used to compute quantities
# #
# #
# #     # #@api.depends('stock_quant_ids.quantity')
# #     # def _compute_quantity(self):
# #     #     quant = self.env['stock.quant'].search([('location_id', '=', 8)])
# #     #
# #     #     for record in self:
# #     #         record.qoh_location1 = 0.0
# #     #         for line in quant.filtered(lambda x: x.product_tmpl_id.id == record.id):
# #     #             record.qoh_location1 += line.quantity