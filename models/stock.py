# -*- coding: utf-8 -*-

#LINE QUE IMPORTA DESDE EL DIRECTORIO OPENERP.OSV
from openerp.osv import osv, fields

class lineas_stock(osv.osv):
	_name = 'co.lineas.stock'
	_description='CO Lineas Stock'

	_columns ={
		'multimedia_id':fields.many2one('co.multimedia','Multimedia'),
		'medio_id':fields.many2one('co.tipo.medio','Medio'),
		'tienda_id':fields.many2one('co.tienda','Tienda'),
		'quantity':fields.integer('Cantidad'),
	}

lineas_stock()


#HERENCIA 
class tienda(osv.osv):
	_inherit = 'co.tienda'

	_columns={
		'line_id':fields.one2many('co.lineas.stock','tienda_id','Stock'),
	}

tienda()