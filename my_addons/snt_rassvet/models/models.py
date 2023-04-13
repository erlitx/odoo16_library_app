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

    # Decorator @api.constrains makes Odoo to call the function when the field 'name' is trying to be saved
    @api.constrains('name')
    def check_name(self):
        if len(self.name) < 5:
            raise exceptions.ValidationError('Name too short')

    # Decorator @api.onchange makes Odoo to call the function when the field 'partner_id' is changed in the form
    # and it returns a new value 'self.mt_contractid = sel[0]' to the field 'mt_contractid' in this from
    # @api.onchange('partner_id')
    # def get_contact(self):
    #     if self.partner_id:
    #         contr = self.env['partner.contract.customer'].search([('partner_id', self.partner_id.id)])
    #     if contr:
    #         sel = contr.sorted(key=lambda r: r.date_start, reverse=True)
    #     if sel:
    #         self.mt_contractid = sel[0]


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
