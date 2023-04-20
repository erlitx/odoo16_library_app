from odoo import fields, models, api
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
    last_borrow_date = fields.Datetime("Last Borrowed On", default=lambda self: fields.Datetime.now())

    # Other fields:
    active = fields.Boolean("Active?", default=True)
    image = fields.Binary("Cover")

    # Relational Fields
    publisher_id = fields.Many2one("res.partner", string="Publisher", index=True)
    author_ids = fields.Many2many("res.partner", string="Authors")

    unit_product_id = fields.Many2one("product.product", string="Unit Product")
    default_code = fields.Char('Default Code', related='unit_product_id.default_code', readonly=True)
    highlighted_id = fields.Reference([('res.partner', 'Partner'), ('res.users', 'User')], string="Highlighted By",)

    # Related field.
    # This is a shortcut for the "publisher_id.country_id" computed field with a method "_compute_publisher_country"
    # It's do the same as the field "publisher_country_id" below
    # It's refer to the "res.country" model becuase the field "publisher_id.country_id" is a chain of Many2one fields leading to
    # the "res.country" model. (library.book) publisher_id -> res.partner (country_id) -> res.country
    publisher_country_id2 = fields.Many2one("res.country", string="Publisher Country (rel)", related="publisher_id.country_id",
                                            readonly=False,)

    # Computed field.
    # Through a compute="" defines that the field is computed field, and it doesn't have a value in the database

    # Inverse="" function call "_inverse_publisher_country" method when the value of the field "publisher_country_id" is changed
    # and change the value of the field "publisher_id.country_id" to the value of the field "publisher_country_id"

    # Search="" function call "_search_publisher_country" method when the value of the field "publisher_country_id" is searched
    # Its needed because the field "publisher_country_id" is computed field and it doesn't have a value in the database, so this trick
    # is used. Instead of this way we can use "stored=True" to make the field "publisher_country_id" stored in the database.
    publisher_country_id = fields.Many2one("res.country", string="Publisher Country", compute="_compute_publisher_country",
                                           inverse="_inverse_publisher_country", search="_search_publisher_country",)


    # The decorator @api.depends() calls the function whenever the value of the field "publisher_id.country_id" changes.
    # When the function is called, the value of the field "publisher_country_id" is updated to all records
    # of "publisher_country_id" in the model. This is because we want to update this ref field (publisher_country_id)
    # to all the records referred to it
    @api.depends("publisher_id.country_id")
    def _compute_publisher_country(self):
        for book in self:
            book.publisher_country_id = book.publisher_id.country_id

    # Inverse function. It takes a value from the field "publisher_country_id" (from view form)
    # and sets it to the field "publisher_id.country_id" which is a county ID of correspondent publisher_id.
    # Note that the field "publisher_country_id" is computed field and get the value from the field "publisher_id.country_id"
    def _inverse_publisher_country(self):
        for book in self:
            book.publisher_id.country_id = book.publisher_country_id

    # Search function called when the value of the field "publisher_country_id" is searched. It returns a valid domain expression
    # like this [('publisher_id.country_id', '=', 1)] which is used to search the records in the database.
    def _search_publisher_country(self, operator, value):
        return [("publisher_id.country_id", operator, value)]

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

    # SQL Constraints. (name, sql_constraint, error_message).
    # UNIQUE constraint: The 'name' and 'date_published' fields must be unique.
    # CHECK constraint: Check the SQL expression (the date_published field must not be in the future)
    _sql_constraints = [("library_book_name_date_uq", "UNIQUE (name, date_published)", "Book title and publication date must be unique."),
                        ("library_book_check_date", "CHECK (date_published <= current_date)", "Publication date must not be in the future."),]

