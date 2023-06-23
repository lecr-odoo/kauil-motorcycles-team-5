from odoo import api, fields, models
from odoo.exceptions import ValidationError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
            # Clean-up the context key at validation to avoid forcing the creation of immediate
            # transfers.
            ctx = dict(self.env.context)
            ctx.pop('default_immediate_transfer', None)
            self = self.with_context(ctx)

            # Sanity checks.
            if not self.env.context.get('skip_sanity_check', False):
                self._sanity_check()

            self.message_subscribe([self.env.user.partner_id.id])

            # Run the pre-validation wizards. Processing a pre-validation wizard should work on the
            # moves and/or the context and never call `_action_done`.
            if not self.env.context.get('button_validate_picking_ids'):
                self = self.with_context(button_validate_picking_ids=self.ids)
            res = self._pre_action_done_hook()
            if res is not True:
                return res

            # Call `_action_done`.
            pickings_not_to_backorder = self.filtered(lambda p: p.picking_type_id.create_backorder == 'never')
            if self.env.context.get('picking_ids_not_to_backorder'):
                pickings_not_to_backorder |= self.browse(self.env.context['picking_ids_not_to_backorder']).filtered(
                    lambda p: p.picking_type_id.create_backorder != 'always'
                )
            pickings_to_backorder = self - pickings_not_to_backorder
            pickings_not_to_backorder.with_context(cancel_backorder=True)._action_done()
            pickings_to_backorder.with_context(cancel_backorder=False)._action_done()

            if self.user_has_groups('stock.group_reception_report'):
                pickings_show_report = self.filtered(lambda p: p.picking_type_id.auto_show_reception_report)
                lines = pickings_show_report.move_ids.filtered(lambda m: m.product_id.type == 'product' and m.state != 'cancel' and m.quantity_done and not m.move_dest_ids)
                if lines:
                    # don't show reception report if all already assigned/nothing to assign
                    wh_location_ids = self.env['stock.location']._search([('id', 'child_of', pickings_show_report.picking_type_id.warehouse_id.view_location_id.ids), ('usage', '!=', 'supplier')])
                    if self.env['stock.move'].search([
                            ('state', 'in', ['confirmed', 'partially_available', 'waiting', 'assigned']),
                            ('product_qty', '>', 0),
                            ('location_id', 'in', wh_location_ids),
                            ('move_orig_ids', '=', False),
                            ('picking_id', 'not in', pickings_show_report.ids),
                            ('product_id', 'in', lines.product_id.ids)], limit=1):
                        action = pickings_show_report.action_view_reception_report()
                        action['context'] = {'default_picking_ids': pickings_show_report.ids}
                        return action
            return True