from xmlrpc import client

url = "https://desarrollokg-odoo-technical-training2-main-5991710.dev.odoo.com"
db = "desarrollokg-odoo-technical-training2-main-5991710"
username = "admin"
password = "admin"

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password, 'academy.session', 'check_access_rights', ['write'], {'raise_exception': False})
print(model_access)

courses = models.execute_kw(db, uid, password, 'academy.course', 'search_read', [[['level', 'in', ['intermediate', 'beginner']]]])