from xmlrpc import client

url = "https://desarrollokg-odoo-technical-training2-main-5991710.dev.odoo.com"
db = "desarrollokg-odoo-technical-training2-main-5991710"
username = "admin"
password = "admin"

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())