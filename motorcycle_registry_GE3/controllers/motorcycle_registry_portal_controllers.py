from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request

class MotorcycleRegistryPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        Registry = request.env['motorcycle.registry']
        if 'registry_count' in counters: #currently broken, registry_count is not being populated in counters variable
            values['registry_count'] = Registry.search_count([]) \
                if Registry.check_access_rights('read', raise_exception=False) else 0

   
        return values
