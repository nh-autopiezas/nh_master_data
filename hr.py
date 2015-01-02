from openerp.osv import osv,fields
from datetime import date
import openerp.addons.decimal_precision as dp


class hr_contract(osv.osv):
        _name = "hr.contract"
        _inherit = "hr.contract"

	def _get_periodo_prueba(self, cr, uid, ids, field_name, arg, context):
		res = {}
		for i in ids:
            		res[i] = False
			contract = self.browse(cr,uid,i)
			if contract.date_end:
				if contract.date_end <= date.today():
				 	res[i] = True
		return res

        _columns = {
		'periodo_prueba' : fields.function(_get_periodo_prueba,type='boolean',string='Periodo Prueba'),
                }

hr_contract()


