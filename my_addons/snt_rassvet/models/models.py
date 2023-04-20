from odoo import fields, models, api, exceptions

class Meeting(models.Model):
    _name = 'snt.meeting'
    _description = "SNT Meeting"
    name = fields.Char(string='Meeting name', required=True)
    date = fields.Datetime(string='Date', required=True)
    question_ids = fields.One2many('snt.question', 'meeting_id', string='Questions')
    member_ids = fields.Many2many('res.users', string='Members')
    protocol_id = fields.Many2one('snt.protocol', string='Protocol')
    test_field = fields.Char("Test")
    members_count = fields.Integer(string='Members number', compute='_onchange_compute_members_count')

    # Decorator @api.constrains makes Odoo to call the function when the field 'name' is trying to be saved
    # Check if the name of the meeting is unique.
    @api.constrains('member_ids')
    def check_name(self):
        # Search for the records with the same name and different id (to exclude the current record)
        existing_record = self.search([('name', '=', self.name), ('id', '!=', self.id)])
        _existing_record = existing_record.browse(existing_record)
        if existing_record:
            names = [rec.name for rec in existing_record]
            message = f"Meeting(s) with name '{', '.join(names)}' already exist!"
            raise exceptions.ValidationError(message)

    # Decorator @api.onchange makes Odoo to call the function when the field 'partner_id' is changed in the form
    # and it returns a new value 'self.mt_contractid = sel[0]' to the field 'mt_contractid' in this from
    @api.onchange('member_ids')
    def _onchange_compute_members_count(self):
        self.members_count = len(self.member_ids)



class Protocol(models.Model):
    _name = 'snt.protocol'
    _description = "SNT Protocol"
    name = fields.Char(string='Protocol name', required = True)
    date = fields.Datetime(string='Date', required = True)
    meeting_id = fields.Many2one('snt.meeting', string='Meeting')
    text = fields.Html(string='Text')
    chairman = fields.Many2one('res.users', string='Chairman')
    secretary = fields.Many2one('res.users', string='Secretary')

class Question(models.Model):
    _name = 'snt.question'
    _description = "SNT Question"
    name = fields.Char(string='Question', required = True)
    yes = fields.Integer(string='Yes')
    state = fields.Selection([('rejected', 'Rejected'), ('accepted', 'Accepted')],
                             string='State', default='rejected')
    meeting_id = fields.Many2one('snt.meeting', string='Meeting')
