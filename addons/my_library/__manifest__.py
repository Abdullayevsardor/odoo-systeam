{
    'name': 'My Library',
    'version': '1.0',
    'summary': 'Birinchi Odoo modulim',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'report/library_book_report.xml',
        'views/library_views.xml',
        'views/hr_employee_views.xml',
    ],
    'application': True,
    'installable': True,
}

