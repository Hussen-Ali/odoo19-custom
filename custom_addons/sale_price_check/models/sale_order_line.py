from odoo import models, fields, api, _
# import logging
# _logger = logging.getLogger(__name__)
from odoo.exceptions import UserError

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # @api.onchange('price_unit')
    # def onchange_price_check(self):
    #     msgs = []
    #
    #     for line in self:
    #         theprice=line.price_unit
    #         msgs.append(f"{"prod_name"}: {theprice}")
    #
    #         _logger.warning("Logger started")
    #         _logger.info(theprice)
    @api.constrains('product_id', 'price_unit')
    def _check_price_vs_cost(self):
        for line in self:
            product = line.product_id
            if product.standard_price:
                if line.price_unit < product.standard_price:
                    raise UserError(
                        _('You cannot sell "%s" below its cost (AVCO: %.2f).')
                        % (product.name, product.standard_price)
                    )



