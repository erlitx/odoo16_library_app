from odoo import api, fields, exceptions, models


class Checkout(models.Model):
    _name = "library.checkout"
    _description = "Checkout Request"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    member_id = fields.Many2one("library.member", string="Member Id", required=True)
    user_id = fields.Many2one("res.users", string="Librarian", default=lambda s: s.env.user)
    request_date = fields.Date(default=lambda s: fields.Date.today(),
                               compute="_compute_request_date_onchange",
                               store=True,
                               readonly=False)
    line_ids = fields.One2many("library.checkout.line", "checkout_id", string="Borrowed Books")

    @api.depends("member_id")
    def _compute_request_date_onchange(self):
        today_date = fields.Date.today()
        if self.request_date != today_date:
            self.request_date = today_date


    @api.model
    def _default_stage_id(self):
        Stage = self.env["library.checkout.stage"]
        return Stage.search([('state', '=', 'new')], limit=1)

    # Here 'group_expand=' is a refference to the  '_group_expand_stage_id' method, and it's called only when
    # the user click on the 'group by' button in the view tree and a view form will pass the parameters
    # 'stages', 'domain', 'order' to the method '_group_expand_stage_id'.
    # If 'group_expand=' parameter is used it override a default behavior of the Group By view.
    # The Default behavior is to only group by stages that have a values in the 'state' field.
    # Now its Group by all the 'state' values in the 'library.checkout.stage' model even if there is no
    # correspondent records in the 'library.checkout' model.
    stage_id = fields.Many2one("library.checkout.stage", string="Stage", default=_default_stage_id,
                               group_expand="_group_expand_stage_id")
    # Reffers to 'stage_id' field and as it a M2O field it reffers then to 'state' field that is a selection field
    # type in library.checkout.stage model.
    state = fields.Selection(related="stage_id.state", string="State")
    checkout_date = fields.Date(string="Checkout Date", readonly=True)
    close_date = fields.Date(string="Close Date", readonly=True)

    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)

    #Check if the newly created record has a valid stage
    @api.model
    def create(self, vals):
        #Creating a new record with the original Class method 'create'
        new_record = super().create(vals)
        if new_record.stage_id.state in ("done", "open"):
            raise exceptions.UserError("Invalid stage for new checkout")
        return new_record


    # # This is an original Odoo method to write any changes to the database/model
    # # Here we are overriding the original method to add some extra functionality - to update the 'checkout_date'
    # # and 'close_date' fields when a user changes the 'stage_id' field.
    # def write(self, vals):
    #     # If there is a key 'stage_id' in the 'vals' dictionary
    #     if "stage_id" in vals:
    #         Stage = self.env["library.checkout.stage"]
    #         # Get 'state' from a current library.checkout record
    #         old_state = self.stage_id.state
    #         # Get a 'state' from the 'stage_id' key in the 'vals' dictionary from the 'library.checkout.stage' model
    #         new_state = Stage.browse(vals["stage_id"]).state
    #         if new_state != old_state and new_state == "open":
    #             vals["checkout_date"] = fields.Date.today()
    #         if new_state != old_state and new_state == "done":
    #             vals["close_date"] = fields.Date.today()
    #         # Now with updated 'vals' dictionary we can call the original 'write' method to save the changes
    #         super().write(vals)
    #         return True

    # This is an original 'write()' Odoo method to write any changes to the database/model
    # Here we are overriding the original 'write()' method to add some extra functionality - to update the 'checkout_date'
    # and 'close_date' fields when user changes the 'stage_id' field.
    # But this time we are using the 'context' parameter to avoid the infinite loop of the 'write()' method
    # because here we are not changing the 'vals' dictionary but using write() method directly to update the
    # 'checkout_date' and 'close_date' fields. If 'context' dict has a key '_checkout_write' with a value 'True',
    # then we are not calling the 'write()' method again.
    def write(self, vals):
        # Get the list of changed fields and their old and new values
        changes = []
        for field_name, new_value in vals.items():
            old_value = getattr(self, field_name)
            if old_value != new_value:
                changes.append((field_name, old_value, new_value))
        # Create the message body with the changed fields
        body = 'The following fields have been changed:'
        for field_name, old_value, new_value in changes:
            body += '\n{}: {} -> {}'.format(field_name, old_value, new_value)
        # Post the message to the form
        self.message_post(subject="Test", body=body)


        # Code before write: `self` has the old values
        old_state = self.stage_id.state
        super().write(vals)
        # Code after write: can use `self` with the updated values
        new_state = self.stage_id.state
        if not self.env.context.get("_checkout_write"):
            if new_state != old_state and new_state == "open":
                self.with_context(_checkout_write=True).write(
                    {"checkout_date": fields.Date.today()})
            if new_state != old_state and new_state == "done":
                self.with_context(_checkout_write=True).write(
                    {"close_date": fields.Date.today()})
        return True

    # # Replaced with compute method in request_date field
    # @api.onchange('member_id')
    # def onchange_member_id(self):
    #    today_date = fields.Date.today()
    #    if self.request_date != today_date:
    #        self.request_date = today_date
    #        return {
    #            'warning': {
    #                'title': 'Changed Request Date',
    #                'message': 'Request date changed to today!',
    #            }
    #        }