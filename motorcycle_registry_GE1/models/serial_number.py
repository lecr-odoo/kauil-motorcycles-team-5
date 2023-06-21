# from odoo import api, fields, models
# from odoo.exceptions import ValidationError

# class GenerateSerialNumber(models.Model):
#     _inherit = ['stock.lot', 'product']
#     name = fields.Char(
#         'Lot/Serial Number', default=lambda self: self.env['ir.sequence'].next_by_code('stock.lot.serial'),
#         required=True, help="Unique Lot/Serial Number", index='trigram', compute='_update_name_if_motorcycle')
#     detailed_type = fields.Selection()


#     @api.depends("name", "detailed_type")
#     def _update_name_if_motorcycle(self):
#         for record in self:
#             if record.detailed_type == "motorcycle":
#                 record.name = record.vin