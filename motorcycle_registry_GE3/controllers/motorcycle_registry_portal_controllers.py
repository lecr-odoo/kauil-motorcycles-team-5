from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request

class MotorcycleRegistryPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        Registry = request.env['motorcycle.registry']
        if 'registry_count' in counters: #currently broken, registry_count is not being populated in counters variable
            domain = self._get_portal_default_domain()
            values['registry_count'] = Registry.search_count(domain)

        return values
