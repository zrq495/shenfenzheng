#!/usr/bin/env python
#coding=utf-8
#FileName: shenfenzheng.py

import web
import pickle
from config import settings
from datetime import datetime

render = settings.render

xishu = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
last_num = [1,0,10,9,8,7,6,5,4,3,2]

class Index:
	def GET(self):
		sdict = {}
		fp1 = open('temp')
		#for line in fp.readline():
			#line = line.split()
			#sdict[line[0]] = line[1]
		#sdict = pickle.load(fp)
		t = fp1.readline()
		if t:
			sdict = eval(t)
		fp1.close()
		return render.index(sdict)

class Inquiry:
	def POST(self):
		fdict = {}
		sdict = {}
		i = web.input()
		haoma = i.get('haoma', None)
		haoma = str(haoma)
		if len(haoma) != 18:
			return render.error('身份证号码不正确，请重新输入!', '/')
		for i in range(len(haoma)-1):
			if haoma[i] > '9' or haoma[i] < '0' :
				return render.error('身份证号码不正确，请重新输入!', '/')
		if haoma[-1] >'9' or haoma[-1] < '0' and (haoma[-1] != 'x' or haoma[-1] != 'X'):
			return render.error('身份证号码不正确，请重新输入!', '/')
		sdict['身份证号码：'] = haoma
		if int(haoma[-2]) % 2:
			sdict['性别：'] = '男'
		else:
			sdict['性别：'] = '女' 
		y, m, d= haoma[6:10],haoma[10:12],haoma[12:14]
		sdict['出生日期：'] = y+'年'+m+'月'+d+'日'
		fp = open('/home/quan/Documents/身份证号码前6位地区对照表')
		for line in fp.readlines():
			line = line.split()
			fdict[line[0]] = line[1]
		sheng = ''
		sheng = fdict[haoma[:2]+"0000"]
		shi = ''
		qu = ''
		if haoma[:2] != '11' and haoma[:2] != '12' and haoma[:2] != '31' and haoma[:2] != '50':
			if haoma[2:4] != '00':
				shi = fdict[haoma[:4]+'00']
		if haoma[4:6] != '00':
			qu = fdict[haoma[:6]]
		sdict['发证地：'] = sheng + ' ' + shi + ' ' + qu
		fp.close()
		sum = 0
		for i in range(17): 
			sum += xishu[i]*int(haoma[i]) 
		yushu = sum % 11
		if haoma[-1] == 'x' or haoma[-1] == 'X':
			haoma[-1] = '10'
		if last_num[yushu] == int(haoma[-1]):
			sdict['校验位：'] = '正确'
		else:
			sdict['校验位：'] = '不正确'
		f = open('temp', 'w')
		f.write(str(sdict))
		f.close()
		raise web.seeother('/')
