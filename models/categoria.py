# -*- coding: utf-8 -*-

#LINE QUE IMPORTA DESDE EL DIRECTORIO OPENERP.OSV
from openerp.osv import osv, fields

class categoria(osv.osv):
	_name = 'co.categoria'
	_description='CO Categoria'

	_columns ={
		'name':fields.char('Nombre'),
		'description':fields.text('Descripción'),
		'parent_id':fields.many2one('co.categoria','Padre'),
		'child_ids':fields.one2many(
			'co.categoria', 
			'parent_id',
			'Sub-categoria'),

	}

categoria()