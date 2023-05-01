# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockQuantOut(models.Model):
    _name = 'stock.quant.out'
    _description = 'Out of stock products'
 #   _inherit = 'stock.quant'

    quant_id = fields.Many2one('stock.quant', string="Quant", )
    quant_out_id = fields.Integer('stock.quant', related='quant_id.id', store=True)
    product_id = fields.Many2one('product.product', string="Product",
                                 related='quant_id.product_id', store=True)
    product_tmpl_id = fields.Many2one('product.template', string="Product Template",
                                      related='quant_id.product_tmpl_id', store=True)
    quantity = fields.Float(string="Quantity", related='quant_id.quantity', store=True)
    location_id = fields.Many2one('stock.location', string="Location", related='quant_id.location_id', store=True)
    location_usage = fields.Selection(string="Location Usage", related='location_id.usage', store=True)
    available_quantity = fields.Float(string="Available Quantity", related='quant_id.available_quantity', store=True)



    # # _auto_init is a method that is called when the module is installed or updated
    # # So when a module is installed or updated, this method will be called and call the 'populate_child_records' method
    @api.model
    def _auto_init(self):
        self.populate_stock_quant_out()
        return super(StockQuantOut, self)._auto_init()

    @api.depends('stock.quant.quantity')
    # self is an active record of the model
    # second arg is a dictionary of arguments from the button's contex when clicked
    def populate_stock_quant_out(self):
        stock_quants = self.env['stock.quant'].search([])
        quant_id_list = self.env['stock.quant.out'].search([]).mapped('quant_id.id')
        for quant in stock_quants:
            if quant.id not in quant_id_list:
                vals = {'quant_id': quant.id, }
                self.env['stock.quant.out'].create(vals)


    # def _update_out_of_stock(self):
    #     new_quantity = self.quantity - self.quantity
    #     quant_id_list = self.env['stock.quant.out'].search([]).mapped('quant_id.id')
    #     for quant in stock_quants:
    #         if quant.id not in quant_id_list:
    #             vals = {'quant_id': quant.id, }
    #             self.env['stock.quant.out'].create(vals)


class StockQuantInherits(models.Model):
    _name = 'stock.quant.out.inherits'
    _description = 'Out of stock products inherits'
    _inherits = {'stock.quant': 'quant_id'}

    quant_id = fields.Many2one('stock.quant', required=True, ondelete='cascade')

class StockQuantInherits(models.Model):
    _description = 'extends stock.quant'
    _inherit = 'stock.quant'

    available_quantity_stored = fields.Float(string="Available Quantity Stored", related='available_quantity', store=True)