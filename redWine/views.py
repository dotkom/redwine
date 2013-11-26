from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, get_object_or_404, redirect
import datetime

def home(request):
    return render(request, 'index.html', {'test' : 1})