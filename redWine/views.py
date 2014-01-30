# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bruker, Straff
import datetime

def home(request):
    wines=6
    straffer=Straff.objects.all()
    brukere=Bruker.objects.all()
    return render(request, 'index.html', {  
        'brukere' : brukere,
        })