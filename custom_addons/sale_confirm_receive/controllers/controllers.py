# from odoo import http


# class SaleConfirmReceive(http.Controller):
#     @http.route('/sale_confirm_receive/sale_confirm_receive', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_confirm_receive/sale_confirm_receive/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_confirm_receive.listing', {
#             'root': '/sale_confirm_receive/sale_confirm_receive',
#             'objects': http.request.env['sale_confirm_receive.sale_confirm_receive'].search([]),
#         })

#     @http.route('/sale_confirm_receive/sale_confirm_receive/objects/<model("sale_confirm_receive.sale_confirm_receive"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_confirm_receive.object', {
#             'object': obj
#         })

