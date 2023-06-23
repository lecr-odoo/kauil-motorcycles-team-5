from odoo import api, fields, models
from geopy.distance import geodesic as GD

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    states_coords = {'AK': (63.588753, -154.493062),
                     'AL': (32.318231, -86.902298),
                     'AR': (35.20105, -91.831833),
                     'AZ': (34.048928, -111.093731),
                     'CA': (36.778261, -119.417932),
                     'CO': (39.550051, -105.782067),
                     'CT': (41.603221, -73.087749),
                     'DC': (38.905985, -77.033418),
                     'DE': (38.910832, -75.52767),
                     'FL': (27.664827, -81.515754),
                     'GA': (32.157435, -82.907123),
                     'HI': (19.898682, -155.665857),
                     'IA': (41.878003, -93.097702),
                     'ID': (44.068202, -114.742041),
                     'IL': (40.633125, -89.398528),
                     'IN': (40.551217, -85.602364),
                     'KS': (39.011902, -98.484246),
                     'KY': (37.839333, -84.270018),
                     'LA': (31.244823, -92.145024),
                     'MA': (42.407211, -71.382437),
                     'MD': (39.045755, -76.641271),
                     'ME': (45.253783, -69.445469),
                     'MI': (44.314844, -85.602364),
                     'MN': (46.729553, -94.6859),
                     'MO': (37.964253, -91.831833),
                     'MS': (32.354668, -89.398528),
                     'MT': (46.879682, -110.362566),
                     'NC': (35.759573, -79.0193),
                     'ND': (47.551493, -101.002012),
                     'NE': (41.492537, -99.901813),
                     'NH': (43.193852, -71.572395),
                     'NJ': (40.058324, -74.405661),
                     'NM': (34.97273, -105.032363),
                     'NV': (38.80261, -116.419389),
                     'NY': (43.299428, -74.217933),
                     'OH': (40.417287, -82.907123),
                     'OK': (35.007752, -97.092877),
                     'OR': (43.804133, -120.554201),
                     'PA': (41.203322, -77.194525),
                     'PR': (18.220833, -66.590149),
                     'RI': (41.580095, -71.477429),
                     'SC': (33.836081, -81.163725),
                     'SD': (43.969515, -99.901813),
                     'TN': (35.517491, -86.580447),
                     'TX': (31.968599, -99.901813),
                     'UT': (39.32098, -111.093731),
                     'VA': (37.431573, -78.656894),
                     'VT': (44.558803, -72.577841),
                     'WA': (47.751074, -120.740139),
                     'WI': (43.78444, -88.787868),
                     'WV': (38.597626, -80.454903),
                     'WY': (43.075968, -107.290284)
                     }

    @api.onchange('partner_shipping_id')
    def _onchange_partner_shipping_id_warehouse(self):
        buffalo_coords = (42.8864, 78.8784)
        sf_coords = (37.7749, 122.4194)
        if self.partner_shipping_id:
            if GD(buffalo_coords, self.states_coords[self.partner_shipping_id.state_id.code]).km < GD(sf_coords, self.states_coords[self.partner_shipping_id.state_id.code]).km:
                self.warehouse_id = self.env['stock.warehouse'].search([('code', '=', 'BUD')]).id
            else:
                self.warehouse_id = self.env['stock.warehouse'].search([('code', '=', 'SFD')]).id

