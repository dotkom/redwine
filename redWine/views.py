# -*- coding: utf-8 -*-
import datetime, re
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
        print(act)
        if act =='add' and int(form.data['amount'])<=10 and len(form.data['reason'])<85:
          #todo: sjekk at man gir til samme komite
          s=Straff(
                  giver=UserProfile.objects.get(user=request.user),
                  to=UserProfile.objects.get(pk=(int(form.data['to'])-1)),
                  amount=int(form.data['amount']),
                  reason=str(form.data['reason'].encode('utf8'))
                  )
          s.save()
          
        elif 'delete' in act: #todo: sjekk at man ikke sletter sin egen
          straffen=Straff.objects.get(pk=int(act.split(" ")[1]))
          if str(straffen.to.user.username) != str(request.user):
            straffen.delete()
        
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