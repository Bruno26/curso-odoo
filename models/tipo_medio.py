# -*- coding: utf-8 -*-

#LINE QUE IMPORTA DESDE EL DIRECTORIO OPENERP.OSV
from openerp.osv import osv, fields

class tipo_medio(osv.osv):
	_name ='co.tipo.medio'
	_description ='CO Tipo Medio'

	_columns ={
		'name':fields.char('Nombre'),
	}

tipo_medio()