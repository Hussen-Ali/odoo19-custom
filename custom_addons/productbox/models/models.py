from odoo import models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        res = super().button_validate()
        self._increment_box()
        return res

    def _increment_box(self):
        BOX_PRODUCT_NAME = "BOX"
        box_product = self.env['product.product'].search([('name', '=', BOX_PRODUCT_NAME)], limit=1)
        if not box_product:
            return

