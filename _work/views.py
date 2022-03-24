from multiprocessing import context
from django.shortcuts import render
from .models import *
from index.pages import pages

# Create your views here.


def index(Request):
    context = {
        'pages': pages,
        'active_page': 'Employment',
        'entries': Entry.objects.all()
    }
    return render(Request, 'work.html', context)

def details(Request, entry):
    active = Entry.objects.get(employer=entry)
    context = {
        'pages': pages,
        'active_page': 'Employment',
        'entries': Entry.objects.all(),
        'active': active
    }
    return render(Request, 'work.html', context)
