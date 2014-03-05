# -*- coding: utf-8 -*-
import datetime, re
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied #change error
from .models import UserProfile, Straff
from .forms import newPenaltyForm


@login_required
def home(request):
    submitted=False
    showDeleted=False
    editedUser=-1
    if request.method == 'POST':
        
        act=str(request.POST['act'])
        form = newPenaltyForm(data=request.POST)
        print(act)
        if act =='add':
          if int(form.data['amount'])<=10 and 1<len(form.data['reason'])<=100:
            #todo: sjekk at man gir til samme komite
            s=Straff(
                    giver=UserProfile.objects.get(user=request.user),
                    to=UserProfile.objects.get(pk=(int(form.data['to'])-1)),
                    amount=int(form.data['amount']),
                    reason=str(form.data['reason'].encode('utf8'))
                    )
            s.save()
            editedUser=int(form.data['to'])-1
          else:
            raise PermissionDenied
            
        elif 'delete' in act: 
          straffen=Straff.objects.get(pk=int(act.split(" ")[1]))
          if str(straffen.to.user.username) != str(request.user):
            straffen.deleted=True
            straffen.save()
            editedUser=straffen.to.user.id
            
        elif 'nuke' in act:
          for straffen in Straff.objects.filter(to=UserProfile.objects.get(pk=int(act.split(" ")[1])-1)):
            if str(straffen.to.user.username) != str(request.user):
              straffen.deleted=True
              straffen.save()
              editedUser=int(act.split(" ")[1])-1
        
        elif 'showhidden' in act:
          showDeleted=True
          editedUser=int(act.split(" ")[1])-2
        
    else:
        form=newPenaltyForm()

    #straffer=Straff.objects.all()
    users=sorted(UserProfile.objects.all(), key=lambda a: a.total(), reverse=True)
    return render(request, 'index.html', {  
        'users' : users,
        'submittedNew' : submitted,
        'showDeleted' : showDeleted,
        'editedUser' : editedUser,
        #'form' : form,
        })