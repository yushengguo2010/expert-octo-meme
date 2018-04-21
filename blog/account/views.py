# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
import datetime

class Login(View):
	def	get(self,request):
		name = u"余嘉欣"
		chenghu = u"同学"
		names = ["Kevin","taka","which"]
		now = datetime.datetime.now()
		# return render(request,'login.html',{"name": name,"chenghu" : chenghu})
		return render(request,"login.html",locals())

# Create your views here.
