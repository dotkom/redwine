# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Straff
from .forms import newPenaltyForm


@login_required
def home(request):
    submitted=False
    if request.method == 'POST':
        
        act=str(request.POST['act'])
        form = newPenaltyForm(data=request.POST)
        print(act+"x")
        if act=='add':
          print(request.user.id)
          print(int(form.data['to']))
          s=Straff(
                  giver=UserProfile.objects.get(id=(request.user.id-1)),
                  to=UserProfile.objects.get(id=(int(form.data['to'])-1)),
                  amount=form.data['amount'],
                  reason=form.data['reason'])
          s.save()
        elif act=='delete':
          pass
        
        elif act=='edit':
          pass
    else:
        form=newPenaltyForm()

    straffer=Straff.objects.all()
    users=UserProfile.objects.all()
    return render(request, 'index.html', {  
        'users' : users,
        'submittedNew' : submitted,
        #'form' : form,
        })