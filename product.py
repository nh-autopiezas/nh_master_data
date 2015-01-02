from openerp.osv import osv,fields
import openerp.addons.decimal_precision as dp


class product_marca(osv.osv):
        _name = "product.marca"
        _description = "Marca"

        _columns = {
                'name': fields.char('Name',size=32),
		'nh_code': fields.char('NH Code',size=20),
                }

product_marca()


class product_modelo(osv.osv):
        _name = "product.modelo"
        _description = "Modelo"

        _columns = {
                'name': fields.char('Name',size=32),
		'nh_code': fields.char('NH Code',size=20),
                }

product_modelo()

class product_subrubro(osv.osv):
        _name = "product.subrubro"
        _description = "SubRubro"

        _columns = {
                'name': fields.char('Name',size=32),
		'nh_code': fields.char('NH Code',size=20),
		'porc_costo': fields.float('% Costo')
                }

product_subrubro()

class product_product(osv.osv):
	_name = "product.product"
	_inherit = "product.product"

	_columns = {
		'nh_code': fields.char('Codigo NH',size=20),
		'nh_supplier_code': fields.char('Codigo Proveedor NH',size=20),
		'supplier_id': fields.many2one('res.partner','Proveedor'),
		'marca_id': fields.many2one('product.marca',string='Marca'),
		'subrubro_id': fields.many2one('product.subrubro',string='Sub-Rubro'),
		'modelo_id': fields.many2one('product.modelo',string='Modelo'),
		}
	
	def name_get(self, cr, user, ids, context=None):
		result = super(product_product,self).name_get(cr,user,ids,context)
		product = self.browse(cr,user,ids)
		cadena = result[0][1]
		if product.subrubro_id.name:
			subrubro = product.subrubro_id.name
		else:
			subrubro = 'N/A'
		product_name = subrubro.strip() + ' / ' + cadena
		result = [(result[0][0],product_name)]
		return result
	

product_product()
