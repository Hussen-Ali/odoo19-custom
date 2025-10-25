from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherits = 'purchase.order.line'
    mybarcode = fields.Char(String = 'myBarcode', related = 'product_id.barcode',readonly=False)
    @api.onchange('mybarcode')
    def _onchange_barcode(self):
        if self.mybarcode:
            self.product_id = self.env['product.product'].search(
                [('mybarcode', '=', self.mybarcode)], limit=1)
