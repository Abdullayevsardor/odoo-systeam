from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Kitob'

    name = fields.Char(string='Sarlavha', required=True)
    author = fields.Char(string='Muallif')
    isbn = fields.Char(string='ISBN')
    publish_date = fields.Date(string='Nashr sanasi')
    pages = fields.Integer(string='Sahifalar soni')
    state = fields.Selection([
        ('available', 'Mavjud'),
        ('borrowed', 'Ijarada'),
        ("lost", "Yo'qolgan"),
    ], default='available', string='Holat')



    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('isbn'):
                vals['isbn'] = 'N/A'
        # ASL create'ni chaqiramiz - bu eng muhim qator
        records = super().create(vals_list)
        return records

    # --- Workflow metodlari (tugmalar shularni chaqiradi) ---

    def action_borrow(self):
        for book in self:
            book.state = 'borrowed'

    def action_return(self):
        for book in self:
            book.state = 'available'

    def action_lost(self):
        for book in self:
            book.state = 'lost'


    librarian_id = fields.Many2one(
        'res.users',
        string='Kutubxonachi',
        default=lambda self: self.env.user,
    )