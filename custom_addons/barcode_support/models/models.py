from odoo import api, fields, models

class PurchaseOrderLines(models.Model):
    _inherit = "purchase.order.line"

    barcode_scan = fields.Char(string='Scanned Barcode', help="Scan barcode to select product")

    @api.onchange('barcode_scan')
    def _onchange_barcode_scan(self):
        if self.barcode_scan:
            product = self.env['product.product'].search([('barcode', '=', self.barcode_scan)], limit=1)
            self.product_id = product if product else False
