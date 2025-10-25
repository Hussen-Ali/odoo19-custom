# from odoo import http


# class CustomAddons/barcodeSupport(http.Controller):
#     @http.route('/custom_addons/barcode_support/custom_addons/barcode_support', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addons/barcode_support/custom_addons/barcode_support/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addons/barcode_support.listing', {
#             'root': '/custom_addons/barcode_support/custom_addons/barcode_support',
#             'objects': http.request.env['custom_addons/barcode_support.custom_addons/barcode_support'].search([]),
#         })

#     @http.route('/custom_addons/barcode_support/custom_addons/barcode_support/objects/<model("custom_addons/barcode_support.custom_addons/barcode_support"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addons/barcode_support.object', {
#             'object': obj
#         })

