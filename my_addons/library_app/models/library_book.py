from odoo import fields, models
from odoo.exceptions import ValidationError


class Book(models.Model):
    """
    Describes a Book catalogue.
    """
    _name = "library.book"
    _description = "Book"

    # Order record for tree view
    _order = "name, date_published desc"

    name = fields.Char("Title", default=None, help="Book cover title.", readonly=False, required=True,
                       index=True, copy=False, groups="", states={},)
    isbn = fields.Char("ISBN")
    book_type = fields.Selection([("paper", "Paperback"), ("hard", "Hardcover"),
                                  ("electronic", "Electronic"), ("other", "Other")], "Type",)
    notes = fields.Text("Internal Notes")
    descr = fields.Html("Description")
    # Numeric fields:
    copies = fields.Integer(default=1)
    avg_rating = fields.Float("Average Rating", (3, 2))
    price = fields.Monetary("Price", "currency_id")
    currency_id = fields.Many2one("res.currency")  # price helper

    # Date and time fields:
    date_published = fields.Date()
    last_borrow_date = fields.Datetime("Last Borrowed On", default=lambda self: fields.Datetime.now(),)

    # Other fields:
    active = fields.Boolean("Active?")
    image = fields.Binary("Cover")

    # Relational Fields
    publisher_id = fields.Many2one("res.partner", string="Publisher", index=True)
    author_ids = fields.Many2many("res.partner", string="Authors")
    # Book <-> Authors relation (using positional args)
    # author_ids = fields.Many2many(
    #     "res.partner",
    #     "library_book_res_partner_rel",
    #     "a_id",
    #     "b_id",
    #     "Authors",
    # )
    # Book <-> Authors relation (using keyword args)
    # author_ids = fields.Many2many(
    #     comodel_name="res.partner",
    #     relation="library_book_res_partner_rel",
    #     column1="a_id",
    #     column2="b_id",
    #     string="Authors")

    unit_product_id = fields.Many2one("product.product", string="Unit Product")
    default_code = fields.Char('Default Code', related='unit_product_id.default_code', readonly=True)


    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError("Please provide an ISBN for %s" % book.name)
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s ISBN is invalid" % book.isbn)
        return True