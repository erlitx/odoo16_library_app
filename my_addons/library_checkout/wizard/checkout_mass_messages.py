from odoo import api, exceptions, fields, models


class CheckoutMassMessage(models.TransientModel):
    _name = "library.checkout.massmessage"
    _description = "Send Message to Borrowers"

    checkout_ids = fields.Many2many("library.checkout", string="Checkouts",)
    message_subject = fields.Char()
    message_body = fields.Html()

    for field in range(5):
        field_name = str(field) + "_field"
        name = field_name
        name = fields.Char(string="Field " + str(field))

    # This method is called when the wizard is opened
    # The default_get method in an Odoo model is used to set default values for the fields of a record
    # that is being created
    @api.model
    def default_get(self, field_names):
        defaults_dict = super().default_get(field_names)
        # Set checkout_ids to the list of active_ids from the context (the list of selected checkouts in a tree view)
        checkout_ids = self.env.context["active_ids"]
        # Set the default values of "checkout_ids" to the checkout_ids list we created above
        defaults_dict["checkout_ids"] = [(6, 0, checkout_ids)]
        return defaults_dict


    def button_send(self):
        self.ensure_one()
        if not self.checkout_ids:
            raise exceptions.UserError(
                "No Checkouts were selected."
            )
        if not self.message_body:
            raise exceptions.UserError(
                "A message body is required"
            )
        for checkout in self.checkout_ids:
            checkout.message_post(
                body=self.message_body,
                subject=self.message_subject,
                subtype_xmlid='mail.mt_comment',
            )

        return True