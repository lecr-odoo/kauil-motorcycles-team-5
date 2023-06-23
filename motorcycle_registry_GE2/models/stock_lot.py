from odoo import api, fields, models
from odoo.exceptions import ValidationError

class StockLot(models.Model):
    _inherit = 'stock.lot'

    registry_id = fields.Many2one(comodel_name='motorcycle.registry', ondelete='restrict') 

