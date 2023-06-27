from odoo import api, fields, models
from odoo.exceptions import ValidationError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        res = self._pre_action_done_hook()
        if res is not True:
            return res
        if self.env.ref('stock.stock_location_customers') == self.location_dest_id:
            for lot in self.move_line_ids.lot_id:
                self.env['motorcycle.registry'].create({
                    'vin': lot.name,
                    'sale_order': self.sale_id.id,
                    'lot_id': lot
                })

        return super(StockPicking, self).button_validate()