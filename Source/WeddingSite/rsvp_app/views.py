from django.shortcuts import *
from django.http import HttpRequest
from django.template import RequestContext
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from datetime import datetime
#from rsvp_app.forms import *
#from rsvp_app.models import *
from django.core.urlresolvers import reverse

from .models import *

# Create your views here.

def index(request):
    assert isinstance(request, HttpRequest)
    context = RequestContext(request)
    return render(
        request,
        'rsvp_app/index.html',
        context
    )

def rsvp(request):
    assert isinstance(request, HttpRequest)
    context = RequestContext(request)
    return render(
        request,
        'rsvp_app/rsvp.html',
        context
                  )
