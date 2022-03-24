from django.shortcuts import render
from .models import *
from index.pages import pages
# Create your views here.

def index(Request):
    context = {
        'pages': pages,
        'active_page': 'Bio',
        'stories': Story.objects.all().order_by('title')
    }
    return render(Request, 'bio.html', context)

def story(Request, story):
    story = Story.objects.get(title=story)
    content = story.content
    content = content.split('<p>')
    context = {
        'pages': pages,
        'active_page': 'Bio',
        'stories': Story.objects.all().order_by('title'),
        'active': story,
        'content': content
    }
    return render(Request, 'bio.html', context)
