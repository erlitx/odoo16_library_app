# -*- coding: utf-8 -*-
# from odoo import http


# class MyAddons/libraryCheckout(http.Controller):
#     @http.route('/my_addons/library_checkout/my_addons/library_checkout', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_addons/library_checkout/my_addons/library_checkout/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_addons/library_checkout.listing', {
#             'root': '/my_addons/library_checkout/my_addons/library_checkout',
#             'objects': http.request.env['my_addons/library_checkout.my_addons/library_checkout'].search([]),
#         })

#     @http.route('/my_addons/library_checkout/my_addons/library_checkout/objects/<model("my_addons/library_checkout.my_addons/library_checkout"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_addons/library_checkout.object', {
#             'object': obj
#         })
