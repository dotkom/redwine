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
        form = newPenaltyForm(request.POST)
        print("hello")
        if form.is_valid(): #ERRORS HERE
            submitted=True
            toUser=UserProfile.objects.get(id=form.cleaned_data['to'])
            print(toUser)
            s=Straff(
                giver=user.username,
                to=toUser,
                amount=form.cleaned_data['amount'],
                reason=form.cleaned_data['reason'])
            s.save()
    else:
        form=newPenaltyForm()

    straffer=Straff.objects.all()
    users=UserProfile.objects.all()
    return render(request, 'index.html', {  
        'users' : users,
        'submittedNew' : submitted,
        'form' : form,
        })