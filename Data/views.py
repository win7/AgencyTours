# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from cms.models import *

from Data.models import *

# Create your views here.
def home(request):
    service = Service.objects.filter(ranking=True)
    data = {
        "service": service
    }
    return render(request, "home.html", data)

def gallery(request):
    service = Service.objects.all()
    service_item = Service.objects.all().distinct('page').order_by('page')
    data = {
        "service_item": service_item,
        "service": service
    }
    return render(request, "gallery.html", data)

def detail(request, args):
    print("detail")
    try:
        service = Service.objects.filter(ranking=True)[:3]
        detail = Service.objects.get(id=args)
        data = {
            "service": service,
            "detail": detail
        }
    except Service.DoesNotExist:
        raise Http404("Not exist...")
    return render(request, "detail.html", data)