from odoo import api, fields, models
from odoo.exceptions import ValidationError

class GenerateSerialNumber(models.Model):
    _inherit = 'stock.lot'
