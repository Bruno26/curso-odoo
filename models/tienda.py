# -*- coding: utf-8 -*-

#LINE QUE IMPORTA DESDE EL DIRECTORIO OPENERP.OSV
from openerp.osv import osv, fields

class tienda(osv.osv):
	_name = 'co.tienda'
	_description = 'CO Tienda'

	_columns={
		'name':fields.char('Tienda'),
		'address':fields.char('Direccion')
	}

tienda()