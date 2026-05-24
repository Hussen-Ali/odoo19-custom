from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('price_unit', 'product_id')
    def _check_unit_price(self):
        if not self.product_id:
            return
        if self.price_unit != self.product_id.lst_price:
            self.price_unit = self.product_id.lst_price  # reset to default
            raise UserError(_('لا يمكنك'))






    # @api.constrains('product_id', 'price_unit')
    # def _check_price_vs_cost(self):
    #     for line in self:
    #         product = line.product_id
    #         if product.standard_price:
    #             if line.price_unit < product.standard_price:
    #                 raise UserError(
    #                     _('You cannot sell "%s" below its cost (AVCO: %.2f).')
    #                     % (product.name, product.standard_price)
    #                 )



