# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def index(request):
 return HttpResponse("<b> ...My Howgood Project... </b>")
 
#def index1(request):
	#cur = connection.cursor()
	#cur.callproc("Ingredient_WinMgr", ['GETNAME'])
	#rr = cur.fetchone()
	#print rr

#def handle_inspection(self, options):
    #connection = connections[options.get('howgood_pcp')]

    #table2model = lambda table_name: table_name.title().replace('_', '').replace(' ', '').replace('-', '')

    #cursor = connection.cursor()
    #cursor.execute("SET search_path TO 'pcp' ")
    # [...]

# Create your views here.
