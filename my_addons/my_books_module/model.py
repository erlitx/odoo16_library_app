from odoo import models, fields, api

class books_in_the_library (models.Model):
    _name = 'library.library_books'
    name = fields.Char(string='Наименование книги)
    author = fields.Char(string='Автор')
    isbn = fields.Char(string='ISBN')
    date_published=fields.Date(string='Дата публикации')
    archived=fields.Boolean(string='Архив')