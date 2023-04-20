from odoo import api, fields, exceptions, models


class CheckoutStage(models.Model):
    _name = "library.checkout.stage"
    _description = "Checkout Stages"
    _order = "sequence"

    name = fields.Char()
    sequence = fields.Integer(default=10)
    fold = fields.Boolean()
    active = fields.Boolean(default=True)
    state = fields.Selection([('new', 'Draft'), ('open', 'Borrowed'),
                              ('done', 'Completed'), ('cancel', 'Canceled')], default='new')

