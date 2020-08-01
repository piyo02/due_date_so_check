{
    'name': 'Due Date Invoice Check',
    'author': "TechnoIndo",
    'category': 'hidden',
    'version': '10.0',
    'summary': 'Addon for check if customer have invocie which due date.',
    'description': '''Addon for check if customer have invocie which due date, and change state of sale_warn to block if true'''
                   ,
    'depends': ['base', 'account'],
    'data': [
        'data/cron.xml'
    ],
    'images': [''],
    'auto_install': False,
    'installable': True,
    'application': False,
}
