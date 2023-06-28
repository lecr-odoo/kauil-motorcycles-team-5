{
    "name": "GE05 Total Motorcycle Mileage",
    
    "summary": "Changing name of motorcycle products to 'year make model'",
    
    "description": """
        Motorcycle Registry
        ====================
        This Module is used to keep track of the Motorcycle Reistration and Ownership of each motorcycled of the brand.
    """,
    
    "version": "0.2",
    
    "category": "Kauil/Registry",
    
    "license": "OPL-1",
    
    "depends": ["website","motorcycle_registry"],

    'data': [
        'views/mileage_snippet.xml'
    ],
    'assets': {
       'web.assets_frontend': [
           '/motorcycle_registry_GE5/static/src/js/mileage_snipp.js',
       ],
    },
    
    "author": "kauil-motors",
    
    "website": "www.odoo.com",
    
    "application": True,
    
}
