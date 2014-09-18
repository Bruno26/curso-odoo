# -*- coding: utf-8 -*-

#LINE QUE IMPORTA DESDE EL DIRECTORIO OPENERP.OSV
from openerp.osv import osv, fields

class lineas_stock(osv.osv):
	_name = 'co.lineas.stock'
	_description='CO Lineas Stock'

	_columns ={
		'multimedia_id':fields.many2one('co.multimedia','Multimedia', required=True),
		'medio_id':fields.many2one('co.tipo.medio','Medio',required=True),
		'tienda_id':fields.many2one('co.tienda','Tienda'),
		'quantity':fields.integer('Cantidad',required=True),
	}

	def onchange_medio_id(self, cr, uid, ids, medio_id):
		return {
			'value':{
				'multimedia_id':False,
				'quantity':0,
			}
		}

	def check_qty(self, cr, uid, ids, context=None):
		#validar que todos los ids sean una lista 
		if isinstance(ids, (int, long)):
			ids =[ids]

		for s in self.browse(cr, uid, ids, context= context):
			if s.quantity < 0:
				return False
		return True

	_constraints = [
		(check_qty, u'No puede guardar un número negativo', ['quantity'])
	]

	_sql_constraints = [
		('stck_medio_tienda', 
			'unique(medio_id,tienda_id, multimedia_id)',
			u'Ya esta definido el stock, actualize')
	]



lineas_stock()

#HERENCIA 
class tienda(osv.osv):
	_inherit = 'co.tienda'

	_columns={
		'line_id':fields.one2many('co.lineas.stock','tienda_id','Stock'),
	}

	#delete en cascada
	def unlink(self, cr, uid, ids, context=None):
		if isinstance(ids, (int, long)):
			ids = [ids]

		for t in self.browse(cr, uid, ids, context= context):
			line_id = [l.id for l in t.line_id]
			if self.pool.get('co.lineas.stock').unlink(cr, uid, line_id):
				if super(tienda, self).unlink(cr, uid, t.id, context= context):
					continue
				return False
			return True
tienda()