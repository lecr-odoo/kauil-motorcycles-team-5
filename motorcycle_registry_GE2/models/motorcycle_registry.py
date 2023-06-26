from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _inherit = 'motorcycle.registry'

    lot_id = fields.One2many(comodel_name="stock.lot", inverse_name="registry_id")
    sale_order = fields.Many2one(comodel_name="sale.order")

    @api.constrains("sale_order")
    def _populate_owner(self):
        if self.sale_order:
            self.owner_id = self.sale_order.partner_id.id

