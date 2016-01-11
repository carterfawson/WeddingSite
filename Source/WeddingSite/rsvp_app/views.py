from django.shortcuts import *
from django.http import HttpRequest
from django.template import RequestContext
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from datetime import datetime
from rsvp_app.forms import *
from rsvp_app.models import *
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    assert isinstance(request, HttpRequest)
    context = RequestContext(request, {
                             'navbar':'index',
                             })
    return render(
        request,
        'rsvp_app/index.html',
        context
    )

def rsvp(request):
    assert isinstance(request, HttpRequest)
    flag = True
    wrong = False
    error = False
    if request.method == 'POST':
        if 'code' in request.POST:
            codeform = RSVP_CodeForm(request.POST)
            if codeform.is_valid():
                if codeform.cleaned_data['code'] == 'celebrationstation':
                    flag = False
                else:
                    wrong = True
            rsvpform = RSVP_Form()
        elif 'rsvp' in request.POST:
            rsvpform = RSVP_Form(request.POST)
            if rsvpform.is_valid():
                flag = True
                addressfull = rsvpform.cleaned_data['address'] + " " + rsvpform.cleaned_data['address2']
                newcont = contact(name=rsvpform.cleaned_data['name'], email=rsvpform.cleaned_data['email'], phone=rsvpform.cleaned_data['phone'], address=addressfull, city=rsvpform.cleaned_data['city'], state=rsvpform.cleaned_data['state'], zip=rsvpform.cleaned_data['zip'], guestnum=rsvpform.cleaned_data['numguests'])
                
                if 'comments' in rsvpform.cleaned_data:
                    newcont.comments=rsvpform.cleaned_data['comments']
                
                if rsvpform.cleaned_data['numguests'] > 1:
                    newcont.attendees=rsvpform.cleaned_data['guestnames']
            
                newcont.save()
                codeform = RSVP_CodeForm()
            else:
                error = True
                codeform = RSVP_CodeForm()
                rsvpform = RSVP_Form()
        else:
            print('security')
    else:
        codeform = RSVP_CodeForm()
        rsvpform = RSVP_Form()
    
    context = RequestContext(request, {
                             'navbar':'rsvp',
                             'flag':flag,
                             'codeform':codeform,
                             'rsvpform':rsvpform,
                             'wrong':wrong,
                             'error':error,
                             })
    return render(
        request,
        'rsvp_app/rsvp.html',
        context
                  )


def details(request):
    assert isinstance(request, HttpRequest)
    context = RequestContext(request, {
                             'navbar':'details',
                             })
    return render(
               request,
               'rsvp_app/details.html',
               context
               )

def about(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = Advice_Form(request.POST)
        if form.is_valid():
            newadv = advice(name=form.cleaned_data['name'], advice=form.cleaned_data['advice'])
            newadv.save()

    form = Advice_Form()

    context = RequestContext(request, {
                             'navbar':'about',
                             'form':form,
                             })
    return render(
               request,
               'rsvp_app/about.html',
               context
               )
