# -*- coding: utf-8 -*-

#LINE QUE IMPORTA DESDE EL DIRECTORIO OPENERP.OSV
from openerp.osv import osv, fields

class multimedia(osv.osv):
	_name = 'co.multimedia'
	_description = 'CO Multimedia'

	_columns={
		'title': fields.char('Título'),
		'release_date': fields.date('Fecha de pubicación'),
		'code': fields.char('Código'),
		'categoria_id';fields.many2one('co.categoria', 'Categoria'),
		'medio_ids': fields.many2many(
			'co.tipo.medio',
			'multimedia_medio_rel',
			'multimedia_id',
			'medio_id'),
	}

multimedia()