from django.shortcuts import render
from project.pages import pages
from .models import *


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
    print(active.positions.all())
    return render(Request, 'work.html', context)
