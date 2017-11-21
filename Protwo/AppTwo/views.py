# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpages_list}
	return render (request, 'index.html', context=date_dict)

def index1(request):
	return render(request, 'index1.htm')

def index2(request):
	return render(request, 'index2.html')

def help(request):
	new_var = {'help': "This content is being printed by templates from the template tag. "}
	return render(request, 'check_dir/help.html', context = new_var)