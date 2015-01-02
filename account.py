from openerp.osv import osv,fields
import openerp.addons.decimal_precision as dp


class res_bank(osv.osv):
	_name = "res.bank"
	_inherit = "res.bank"

	_columns = {
		'nh_code': fields.char('Codigo NH',size=20),
		}

res_bank()
