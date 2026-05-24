
{
    'name': "Pos Order Line IQD",
    'version': '19.0.1.0.0',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'assets': {
            'point_of_sale._assets_pos': [
                'pos_order_line_image/static/src/xml/pos_order_line.xml',
            ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
