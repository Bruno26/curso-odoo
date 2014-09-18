# -*- coding: utf-8 -*-

#LINE QUE IMPORTA DESDE EL DIRECTORIO OPENERP.OSV
from openerp.osv import osv, fields


class suscriptor(osv.osv):
	_name = 'co.suscriptor'
	_decription = 'CO Suscriptor'

	_columns = {
		'name': fields.char('Nombre'),
		'identification': fields.char('Cédula'),
		'address': fields.text('Dirección'),
	}

	_sql_constraints=[
		('identification_uniq', 'unique(identification)', 
			u'Ya existe el número de cédula.'),
	]

suscriptor()