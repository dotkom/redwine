# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Straff


@login_required
def home(request):
    wines=6
    straffer=Straff.objects.all()
    users=UserProfile.objects.all()
    return render(request, 'index.html', {  
        'users' : users,
        'isAdmin' : True,
        })