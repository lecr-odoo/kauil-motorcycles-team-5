from odoo import models

class ApplyDiscount(models.Model):
    _name = "apply.discount"
    _inherit = "sales.order"

    def apply_discount(self):
        return True