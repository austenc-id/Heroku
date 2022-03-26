from django.shortcuts import render
from project.pages import pages
from .models import Group


def index(Request):
    context = {
        'pages': pages,
        'active_page': 'Education',
        'groups': Group.objects.all().order_by('title')
    }
    return render(Request, 'education.html', context)

def group(Request, group):
    group = Group.objects.get(title=group)
    context = {
        'pages': pages,
        'active_page': 'Education',
        'groups': Group.objects.all().order_by('title'),
        'active': group,
    }
    return render(Request, 'education.html', context)