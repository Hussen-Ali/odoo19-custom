from odoo import models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm_and_receive(self):
        self.action_confirm()

        pickings = self.mapped('picking_ids')
        if not pickings:
            return {'type': 'ir.actions.act_window_close'}

        for picking in pickings:
            if picking.state not in ('done', 'cancel'):
                picking.action_confirm()
                picking.action_assign()
                picking.button_validate()

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

        action = self.env.ref('stock.action_picking_tree_all').sudo().read()[0]
        action['domain'] = [('id', 'in', pickings.ids)]
        return action
