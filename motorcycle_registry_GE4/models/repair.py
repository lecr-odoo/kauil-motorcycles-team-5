from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Repair(models.Model):
    _inherit = 'repair.order'

    vin = fields.Char(string='VIN')
    current_mileage = fields.Float(string='current_mileage')
    registry_id = fields.Many2one(comodel_name='motorcycle.registry', string='Registry ID', compute='_get_registry_id_from_vin')

    # The following fields are overrode to be related to registry_id.
    partner_id = fields.Many2one(relatiion='registry_id')
    sale_order_id = fields.Many2one(relation='registry_id')
    product_id = fields.Many2one(relation='registry_id')

    @api.depends('vin')
    def _get_registry_id_from_vin(self):
        for record in self:
            registry_entry = record.env['motorcycle.registry'].search([('vin', '=', record.vin)])
            if registry_entry:
                record.registry_id = registry_entry
            else:
                record.registry_id = False

    # @api.depends('vin')
    # def _get_registry_id_from_vin(self):
    #     pass
