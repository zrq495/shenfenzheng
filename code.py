#!/usr/bin/env python
#coding=utf-8
#FileName: code.py

from config.url import urls
import web

app = web.application(urls, globals())

if __name__ == "__main__":
	app.run()
