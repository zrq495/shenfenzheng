#!/usr/bin/env python
#coding=utf-8
#FileName: settings.py

import web

render = web.template.render('templates/',cache=False)

web.config.debug = True

config = web.storage(
		email = 'zrq495@gmail.com',
		site_name = '身份证查询',
		site_desc = '',
		static = '/static',
		)

web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
