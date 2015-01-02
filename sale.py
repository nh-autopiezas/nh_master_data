from openerp.osv import osv,fields
from datetime import date
import openerp.addons.decimal_precision as dp


class sale_order(osv.osv):
        _name = "sale.order"
        _inherit = "sale.order"

        _columns = {
		'margin': fields.float('Margin', digits=(16,2))
                }

sale_order()


class sale_order_line(osv.osv):
        _name = "sale.order.line"
        _inherit = "sale.order.line"

        _columns = {
		'business_line': fields.selection((('new','new'),('recycled','recycled')),string='Business Line') 
                }

sale_order_line()
