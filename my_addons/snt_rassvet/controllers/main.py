from odoo import http
from odoo.http import request

class SNT(http.Controller):

    @http.route("/snt2")
    def list(self, **kwargs):
        Book = http.request.env["library.book"]
        books = Book.search([])
        return http.request.render("library_app.book_list_template", {"books": books})


    @http.route('/snt', auth='public')
    def index(self, **kw):
        return "Hello, world!"

    @http.route('/snt_members', auth='public', website=True)
    def hello(self, **kwargs):
        Meeting = http.request.env["snt.meeting"]
        meetings = Meeting.search([])
        return request.render('snt_rassvet.hello', {'meetings': meetings})