# -*- coding: utf-8 -*-

#LINE QUE IMPORTA DESDE EL DIRECTORIO OPENERP.OSV
from openerp.osv import osv, fields

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

	#AGREGANDO LAS COLUMNAS DE LA TABLA DE UN MODULO
	_columns = {
		'code':fields.char('Código'),
		'type': fields.selection(TIPO, 'Tipo de Suscripcion'),
		'date_start':fields.date('Inicio suscripcion'),
		'date_end':fields.date('Fin suscripcion'),
		'active':fields.boolean('Activo'),
		'suscriptor_id':fields.many2one('co.suscriptor','Afiliado'),
	}


suscripcion()
