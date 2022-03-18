from django.shortcuts import render
from _home.models import Link, Page
from .models import Category
# Create your views here.

def index(Request):
    context = {
        'links': Link.objects.all(),
        'pages': Page.objects.all(),
        'page': Page.objects.get(label='education'),
        'categories': Category.objects.all()
    }
    return render(Request, 'pages/edu.html', context)