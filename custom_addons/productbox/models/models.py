from odoo import models, fields, api


class ProductBox(models.Model):
    _inherit = 'product.template'

    product_box = fields.Char("Product Box", required=True)


