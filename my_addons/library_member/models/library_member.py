from odoo import fields, models

# Create a deligated Model
class Member(models.Model):
    _name = "library.member"
    _description = "Library Member"
    # Addind the mail.thread and mail.activity.mixin classes to out Model (we'll be able to add mail threads and
    # activities to our form view)
    _inherit = ["mail.thread", "mail.activity.mixin"]

    card_number = fields.Char()
    # Get a deligtion inherinatse from the res.partner model. Now if a new recod for Member ('library.member') is created,
    # a new record for res.partner is created as well.
    # This is actually a one-to-one relationship between the two models, but Odoo does not support one-to-one relationships
    # so many2one is used instead.
    partner_id = fields.Many2one("res.partner", delegate=True, ondelete="cascade", required=True)

