# -*- coding: utf-8 -*-
import datetime, re
from operator import itemgetter
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.conf import settings
from django.core.exceptions import PermissionDenied #change error 
from django.db.models import Q
from .models import Penalty
from .forms import newPenaltyForm
from django.contrib.auth import get_user_model
from django.db.models import Prefetch


@login_required
def redwine_home(request):
    try:
        return redwine_com(request, request.user.groups.filter(pk__in=settings.USER_SEARCH_GROUPS)[0])
    except(IndexError):
        return render(request, 'redwine/index.html', { "error":True, "errorMessage":"You have no active redwine committees!"})

def redwine_com(request, committee):
    User = get_user_model()
    submitted=False
    showDeleted=False
    ownDelete=False
    editedUser=-1
    try:
        kom = request.user.groups.filter(name=committee)[:1].get();
    except:                                                             #TODO: handle exception better!
        return render(request, 'redwine/index.html', { 
            "error":True, 
            "errorMessage":"You don't have access to this committee. If you think you should, please contact a sysadmin."
            })

    if request.method == 'POST':
        act=str(request.POST['act'])
        form = newPenaltyForm(data=request.POST)
        if act =='add':
            if int(form.data['amount'])<=10 and 1<len(form.data['reason'])<=100:
                #todo: sjekk at man gir til samme komite
                item=form.data['type'].split(".")
                if len(item)<1:
                    return

                s=Penalty(
                    giver=     request.user,
                    committee= form.data['committee'],
                    to=        User.objects.get(pk=(int(form.data['to']))),
                    amount=    int(form.data['amount']),
                    reason=    form.data['reason'],
                    item=      item[0],
                    item_name= item[1]
                    )
                s.save()
                editedUser=int(form.data['to'])
            else:
                return render(request, 'redwine/index.html', { "error":True, "errorMessage":"The reason must be between 1 and 100 chars."})
                
        elif 'delete' in act: 
            #filter for koms
            penalty=Penalty.objects.get(pk=int(act.split(" ")[1]))
            if str(penalty.to.id) != str(request.user.id):
                penalty.deleted=True
                penalty.save()
                editedUser=penalty.to.id

        elif 'nuke' in act:
            #filter for kom
            for penalty in Penalty.objects.filter(to=User.objects.get(pk=int(act.split(" ")[1]))):
                if str(penalty.to.id) != str(request.user.id):
                    penalty.deleted=True
                    penalty.save()
                    editedUser=int(act.split(" ")[1])
                else:
                    ownDelete=True

        elif 'showhidden' in act:
            showDeleted=True
            editedUser=int(act.split(" ")[1])

        else:
            form=newPenaltyForm()

    committees = {} #move total into loop if multiple coms in one page
    total = lambda user: sum([penalty.amount for penalty in user.penalties.filter(deleted=False, committee=com)])
    by_kom= lambda user: user.penalties.filter(deleted=False, committee=com)
    for com in request.user.groups.filter(pk__in=settings.USER_SEARCH_GROUPS):
        if com==kom:
            
            committees[com] = [(user, total(user), by_kom(user)) for user in com.user_set.all()] 
            committees[com].sort(key=itemgetter(1),reverse=True)
        else:
            committees[com] = (0,0,0)

    return render(request, 'redwine/index.html', {  
        'committees'   : committees,
        'currCom'      : kom,
        'submittedNew' : submitted,
        'showDeleted'  : showDeleted,
        'editedUser'   : editedUser,
        'ownDelete'    : ownDelete,
        #'form' : form,
        })


def total_unflitered(user):
    return sum([penalty.amount for penalty in user.penalties.all()])


def redwine_top(request):
    User = get_user_model()

    # check if in com
    try:
        kom = request.user.groups.filter(pk__in=settings.USER_SEARCH_GROUPS)[:1].get()
    except:                                                             #TODO: handle exception better!
        return render(request, 'redwine/index.html', { 
            "error": True, 
            "errorMessage": "You are not in any commitee"
            })

    committees = {} # move total into loop if multiple coms in one page
    
    kom = "top"
    for com in request.user.groups.filter(pk__in=settings.USER_SEARCH_GROUPS):
        committees[com] = (0, 0, 0)

    penalties = Penalty.objects.filter(amount__lt=9).prefetch_related(
        Prefetch('to', queryset=User.objects.all()),
        Prefetch('giver', queryset=User.objects.all()),
    )

    top = {}
    for penalty in penalties:
        username = penalty.to.username
        if penalty.amount < 9:  # dont count "fake" penalties
            if username not in top:
                top[username] = [penalty.to, penalty.amount, [penalty]]
            else:
                top[username][1] += penalty.amount
                top[username][2].append(penalty)

    top = list(top.values())
    top.sort(key=itemgetter(1), reverse=True)
    if len(top) > 20:
        top = top[:20]

    return render(request, 'redwine/top.html', {  
        'committees'   : committees,
        'currCom'      : kom,
        'top'          : top,
        })