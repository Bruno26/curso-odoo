# -*- coding: utf-8 -*-

#Diccionario necesario para crear u n moduloe en 0penERP

{
	'name': 'Curso OpenEPR',
	'description': 'Este módulo es para aprender en OpenEPR',
	'author':'Bruuno Palacios',
	'version':'dia1',
	'depends': ['base', 'mail', ],
	'data': [
		'views/curso_odoo_view.xml',
		'views/multimedia_view.xml',
		'views/tipo_medio_view.xml',
		'views/tienda_view.xml',
		'views/categoria_view.xml',
		'views/suscriptor_view.xml',
		'views/suscripcion_view.xml',
		'views/solicitud_view.xml',
		'data/suscripcion_data.xml',
	],
	'demo': [],
}
