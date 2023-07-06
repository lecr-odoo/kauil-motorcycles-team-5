from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_new_customer = fields.Boolean(compute = '_compute_is_new_customer')
    
    @api.depends('order_line.product_template_id.detailed_type', 'partner_id' )
    def _compute_is_new_customer(self):
        for sale_order in self:
            is_buying_motorcycle = any([order_line.product_template_id.detailed_type == 'motorcycle' for order_line in sale_order.order_line])
            other_orders = self.env['sale.order'].search([('id', 'not in', sale_order.ids), ('state', '=', 'sale'), ('partner_id.id', '=', sale_order.partner_id.id)])
            first_time_buyer = 'motorcycle' not in other_orders.mapped('order_line.product_template_id.detailed_type')
           
            sale_order.is_new_customer = is_buying_motorcycle and first_time_buyer

    def apply_discount(self):
        self.pricelist_id = self.env['product.pricelist'].search([('name', '=', 'Motorcycle Discount')])[0]