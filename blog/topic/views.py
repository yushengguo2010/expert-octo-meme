# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,reverse
from django.views import View

class Topic(View):
	def	get(self,request,tid):
		topics = {
			1:"a novel here.",
			2:"a romantic story here",
			3:"a scientific novel here"
		}
		print "Find a topic"
		print topics[int(tid)]
		# return redirect(reverse("account:login"))
		return render(request,'topics.html')

def page_not_found(request):
	return render(request,"404.html")