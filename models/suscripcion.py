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
class tipo_suscripcion(osv.osv):
	_name = 'co.tipo.suscripcion'
	_description ='CO Tipo Suscripcion'

	_columns = {
		'name': fields.char('Nombre'),
		'medio_ids':fields.many2many(
			'co.tipo.medio',
			'tipo_suscripcion_medio_rel',
			'tipo_id',
			'medio_id'),
	}

	__sql_constraints =[
		('name_uniq', 'unique(name)', 'El nombre no puede repertirse')
	]

class suscripcion(osv.osv):
	#CAMPOS OBLIGATORIOS , RESERVADOS
	_name = 'co.suscripcion'
	_description = 'CO Suscripcion'
	_rec_name = 'code'

	#AGREGANDO LAS COLUMNAS DE LA TABLA DE UN MODULO
	_columns = {
		'code':fields.char('Código', help='El codigo se genera de manera automatica...'),
		#'type': fields.selection(TIPO, 'Tipo de Suscripcion', required=True),
		'type': fields.many2one('co.tipo.suscripcion', 'Tipo de Suscripcion', required=True),
		'date_start':fields.date('Inicio suscripcion', required=True),
		'date_end':fields.date('Fin suscripcion', required=True),
		'active':fields.boolean('Activo'),
		'suscriptor_id':fields.many2one('co.suscriptor','Afiliado', required=True),
	}

	_defaults={
		'active':True,
		'date_start':datetime.now().strftime('%Y-%m-%d'),
	}

	# FUNCTION QUE VALIDA QUE LA FECHA END NO SEA MAYOR QUE LA FECHA START
	# TODA FUNCION QUE COMIENZE CON _ SON FUNCUINES PRIVADAS DEL MODELO 
	def _check_dates(self, cr, uid, ids, context=None):
		# CONVERTE TODAS LAS ENTRADAS EN IN LISTA PAARA EVITAR ERROR 
		if isinstance (ids ,(int, long)):
			ids = [ids]

		for s in self.browse(cr, uid, ids, context=context):
			if s.date_end <= s.date_start:
				return False
		return True

	_constraints = [
		(_check_dates, 'Fecha de inicio debe ser menor a fecha final',
			['date_start', 'date_end'])
	]

	#funcion que crea el code secuencial 
	def create(self, cr, uid, values, context=None):
		if context is None:
			context = {}

		values.update({
			'code': self.pool.get('ir.sequence').get(cr, uid,'seq.suscripcion')})
		return super(suscripcion,self).create(cr, uid, values, context=context)

suscripcion()



class suscriptor(osv.osv):
	_inherit = 'co.suscriptor'

	_columns = {
		'suscripcion_ids':fields.one2many(
			'co.suscripcion',
			'suscriptor_id'),
	}
	
suscriptor()