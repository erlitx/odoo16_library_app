# -*- coding: utf-8 -*-
# from odoo import http

# class CrmTest(http.Controller):
#     @http.route('/crm_test/crm_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_test/crm_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_test.listing', {
#             'root': '/crm_test/crm_test',
#             'objects': http.request.env['crm_test.crm_test'].search([]),
#         })

#     @http.route('/crm_test/crm_test/objects/<model("crm_test.crm_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_test.object', {
#             'object': obj
#         })
