from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'   # _name EMAS, _inherit

    library_card_number = fields.Char(string='Kutubxona kartasi')