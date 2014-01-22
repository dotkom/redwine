# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, get_object_or_404, redirect
import datetime

def home(request):
    wines=6
    return render(request, 'index.html', {  
        'username' : 'Nicolas Tester',
        'wines' : wines,
        'wineList' : range(3),
        'wineString' : str(wines),
        'isAdmin' : True,
        'name' : 'Nicolas Mifadutti Poppy',
        'time' : '2014-01-15 13:37',
        'author' : 'Nils',
        'reason' : 'Spiste for mye pizza og sendte ikke nok pupper på snap.'
        })