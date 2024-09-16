{
    'name': 'Cálculo de Caja',
    'version': '1.0',
    'summary': 'Módulo para el cálculo de caja',
    'description': 'Este módulo permite realizar cálculos de caja basados en entradas y salidas.',
    'category': 'Accounting',
    'author': 'Tu Nombre',
    'website': 'https://www.tuempresa.com',
    'license': 'LGPL-3',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/caja_calculo_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'caja_calculo/static/src/js/caja_calculo.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
