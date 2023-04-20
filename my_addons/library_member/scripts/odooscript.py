import odoorpc
from odoo_rpc_client import Client
from datetime import datetime, timedelta

HOST = 'backoffice.amperka.ru'
DATABASE = 'production'
USERNAME = ''
PASSWORD = ''
PORT = 443
env = Client(HOST, DATABASE, USERNAME, PASSWORD, PORT, protocol="json-rpcs" if PORT == 443 else "json-rpc",)
v
today = datetime.now().date()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')
today_str = today.strftime('%Y-%m-%d')
tomorrow_str = tomorrow.strftime('%Y-%m-%d')


Partner = env['res.partner']

partners_ids = Partner.search([('create_date', '>=', yesterday_str), ('create_date', '<', tomorrow_str)])
partners = Partner.browse(partners_ids)
for partner in partners:
    print(partner.name)

# fields = Partner.fields_get()
# field_names = list(fields.keys())
# print(field_names)
#('location_id.name', '=', 'AMPRU/Stock')







# Quant = env["stock.quant"]
#
# inventory_ids = Quant.search([('location_id.id', '=', '141')], order='__last_update desc', limit=100)
# inventory = Quant.browse(inventory_ids)
# for item in inventory:
#     print(f'{item.id} - {item.create_date} - {item.location_id.display_name} - '
#           f'{item.product_id.default_code} - {item.product_id.name} - {item.quantity} - '
#           f'{item.__last_update} - {item.location_id.id}')
#
#
# fields = Quant.fields_get()
# field_names = list(fields.keys())
# print(field_names)
#
# Locations = env["stock.location"]
# fields = Locations.fields_get()
# field_names = list(fields.keys())
# print(field_names)
#
# #location_ids = Locations.search([('id', '=', '141')])
# locations = Locations.browse(141)
# print(locations.name)






# # Use all methods of a model
# if 'sale.order' in odoo.env:
#     Order = odoo.env['sale.order']
#     order_ids = Order.search([])
#     for order in Order.browse(order_ids):
#         print(order.name)
#         products = [line.product_id.name for line in order.order_line]
#         print(products)
