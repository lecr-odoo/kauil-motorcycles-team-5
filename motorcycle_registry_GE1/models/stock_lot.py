
from re import findall as regex_findall, split as regex_split

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StockLot(models.Model):
    _inherit = 'stock.lot'

    def _compute_prefix_from_vin(self, product):
        """
        Return the prefix of the serial number for motorcycle product
        by using the format of VIN, i.e. Make + Model + Year.
        """
        return (product.make[:2] + product.model[:2]).upper() + str(product.year)[2:] + product.battery_capacity.upper()
    
    @api.model
    def _get_next_serial(self, company, product):
        """Return the next serial number to be attributed to the product."""
        if product.tracking != "none" and product.product_tmpl_id.detailed_type == 'motorcycle':
            serial_number_prefix = self._compute_prefix_from_vin(product)
            return serial_number_prefix + self.env['ir.sequence'].next_by_code('stock.lot.serial')
        else:
            return super(StockLot, self)._get_next_serial(company, product)

    # @api.model
    # def _get_next_serial(self, company, product):
    #     """Return the next serial number to be attributed to the product."""
    #     if product.tracking != "none":
    #         last_serial = self.env['stock.lot'].search(
    #             [('company_id', '=', company.id), ('product_id', '=', product.id)],
    #             limit=1, order='id DESC')
    #         if last_serial:
    #             serial_number = self.env['stock.lot'].generate_lot_names(last_serial.name, 2)[1]
    #             if product.product_tmpl_id.detailed_type == 'motorcycle':
    #                 serial_number_prefix = self._compute_prefix_from_vin(product)
    #                 serial_number_suffix = serial_number[-6:]
    #                 serial_number = serial_number_prefix + serial_number_suffix
    #                 return serial_number
    #             else:
    #                 return serial_number
    #     return False
    