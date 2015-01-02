from openerp.osv import osv,fields
import openerp.addons.decimal_precision as dp


class res_users(osv.osv):
	_name = "res.users"
	_inherit = "res.users"

	_columns = {
		'nh_code': fields.char('Codigo NH',size=20),
		}

res_users()
