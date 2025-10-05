from odoo import models, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm_and_receive(self):
        self.action_confirm()  # Confirm the SO

        # Fetch related pickings (delivery orders)
        pickings = self.mapped('picking_ids')
        if not pickings:
            return {'type': 'ir.actions.act_window_close'}

        # Automatically validate the picking(s)
        for picking in pickings:
            if picking.state not in ('done', 'cancel'):
                # Force validate picking (mark as done)
                picking.action_confirm()  # confirm picking
                picking.action_assign()   # reserve products
                picking.button_validate() # validate picking

        # If there is only one picking, open it in form view (optional)
        if len(pickings) == 1:
            picking = pickings[0]
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'view_mode': 'form',
                'res_id': self.id,
                'views': [(self.env.ref('sale.view_order_form').id, 'form')],
                'target': 'current',
            }

        # If multiple pickings, show tree view
        action = self.env.ref('stock.action_picking_tree_all').sudo().read()[0]
        action['domain'] = [('id', 'in', pickings.ids)]
        return action
