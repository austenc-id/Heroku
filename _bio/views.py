from django.shortcuts import render
from .models import *
# Create your views here.

def index(Request):
    context = {
        'page': 'bio',
        'stories': Story.objects.all()
    }
    return render(Request, 'bio.html', context)

def story(Request, story):
    context = {
        'page': 'bio',
        'stories': Story.objects.all(),
        'active': Story.objects.get(title=story)
    }
    return render(Request, 'bio.html', context)