from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _inherit = ['portal.mixin', 'motorcycle.registry']
    _name = 'motorcycle.registry'
