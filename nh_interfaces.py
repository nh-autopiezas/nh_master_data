from openerp.osv import osv,fields
import openerp.addons.decimal_precision as dp


class nh_interface(osv.osv):
	_name = "nh.interface"
	_description = "Proceso a correr interfaces"

	_columns = {
		'proceso': fields.char('Proceso',size=20),
		'fecha_sistema': fields.integer('Fecha Sistema',size=20),
		}

nh_interface()

class nh_interface_process(osv.osv):
	_name = "nh.interface.process"
	_description = "Proceso a correr interfaces"

	_columns = {
		'interface_id': fields.many2one('nh.interface','Interface'),
		'date': fields.date('Fecha de proceso'),
		'result': fields.selection((('OK','OK'),('Error','Error')),'Result')
		}

nh_interface_process()
