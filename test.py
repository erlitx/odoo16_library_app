from odoo import api, models

# Assuming this code is inside a method of some Odoo model, you can use the self.env attribute to get the Odoo environment
env = self.env

# Use the browse method of the res.partner model to retrieve a record with ID 40
partner = env['res.partner'].browse([40])

# Get the name of the record and print it
name = partner.name
print(name)