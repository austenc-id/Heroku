from django.shortcuts import render
from .models import Link, Page
# Create your views here.

def index(Request):
    context = {
        'links': Link.objects.all(),
        'pages': Page.objects.all(),
        'page': Page.objects.get(label='home')
    }
    return render(Request, 'pages/home.html', context)