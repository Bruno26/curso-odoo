# -*- coding: utf-8 -*-

#LINE QUE IMPORTA DESDE EL DIRECTORIO OPENERP.OSV
from openerp.osv import osv, fields
from datetime import datetime

#TUPLA EN DONDE SE DEFINE EL CAMPO SELECT PROVINIENTE DESDE LA VISTA
TIPO = [
	('oro','Plan ORO'),
	('plarta','Plan PLATA'),
	('bronce','Plan BRONCE'),
]

class suscripcion(osv.osv):
	#CAMPOS OBLIGATORIOS , RESERVADOS
	_name = 'co.suscripcion'
	_description = 'CO Suscripcion'
	_rec_name = 'code'

	#AGREGANDO LAS COLUMNAS DE LA TABLA DE UN MODULO
	_columns = {
		'code':fields.char('Código'),
		'type': fields.selection(TIPO, 'Tipo de Suscripcion'),
		'date_start':fields.date('Inicio suscripcion'),
		'date_end':fields.date('Fin suscripcion'),
		'active':fields.boolean('Activo'),
		'suscriptor_id':fields.many2one('co.suscriptor','Afiliado'),
	}

	_defaults={
		'active':True,
		'date_start':datetime.now().strftime('%Y-%m-%d'),
		#'code': lambda self, cr, uid, context: self.pool.get('ir.sequence').get(cr, uid,'seq.suscripcion'),
	}


	#funcion que crea el code secuencial 
	def create(self, cr, uid, values, context=None):
		if context is None:
			context = {}

		values.update({
			'code': self.pool.get('ir.sequence').get(cr, uid,'seq.suscripcion')})
		return super(suscripcion,self).create(cr, uid, values, context=context)

suscripcion()