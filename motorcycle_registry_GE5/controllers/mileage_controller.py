from odoo import http
from odoo.http import request

class Sales(http.Controller):
    @http.route(['/total_product_sold'], type="json", auth="public")
    def sold_total(self):
        # sale_obj = request.env['sale.order'].sudo().search([
        #    ('state', 'in', ['done', 'sale']),
        # ])
        total_sold = 555
        return total_sold