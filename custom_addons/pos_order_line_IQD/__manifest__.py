
{
    'name': "Pos Order Line IQD",
    'version': '19.0.1.0.0',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_order_line_IQD/static/src/xml/pos_order_line.xml",
            "pos_order_line_IQD/static/src/xml/pos_receipt.xml",
            "pos_order_line_IQD/static/src/css/receipt_spacing_fix.css",
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
