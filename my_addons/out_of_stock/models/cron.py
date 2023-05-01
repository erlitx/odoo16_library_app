from odoo import api, SUPERUSER_ID

def _setup_cron_jobs(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.cron'].sudo().create({
        'name': 'Populate child records',
        'interval_number': 1,
        'interval_type': 'minutes',
        'numbercall': -1,
        'doall': True,
        'active': True,
        'model': 'stock.quant.out',
        'function': 'populate_child_records',
    })
