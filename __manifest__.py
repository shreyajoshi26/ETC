
{
    'name': 'Electronic Toll Collection',
    'version': '1.0',
    'category': 'management',
    'sequence': 15,
    'summary': 'Electronic Toll Collection system',
    'data':[
            'views/etc.xml',
            'views/website.xml'
    ],
    'depends': ['base','website_sale'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
