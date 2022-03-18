from django.shortcuts import render
from _home.models import Link, Page
from .models import Entry
# Create your views here.

def index(Request):
    context = {
        'links': Link.objects.all(),
        'pages': Page.objects.all(),
        'page': Page.objects.get(label='bio'),
        'entries': Entry.objects.all()
    }
    return render(Request, 'pages/bio.html', context)