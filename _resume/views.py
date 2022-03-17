from django.shortcuts import render
from .models import *
# Create your views here.
context = {
    'title': 'austen c. myers',
    'subtitle': 'professional profile',
    'links': [
        {
        'label': 'github',
        'url': 'https://github.com/austenc-id'
        },
        {
        'label': 'linkedIn',
        'url': 'https://www.linkedin.com/in/austenc-id/'
        },
        {
        'label': 'resume',
        'url': 'static/downloads/resume.pdf'
        }
    ],
    'sections': [
        {
        'label': 'bio',
        'link': 'resume:bio',
        },
        {
        'label': 'employment',
        'link': 'resume:employment'
        },
        {
        'label': 'education',
        'link': 'resume:education'
        },
        {
        'label': 'skills',
        'link': 'resume:skills'
        }
        ],
    }
def bio(REQUEST):
    journal = Journal.objects.get(journal_id=1)
    context.update({
        'blurb': 'A little about me.',
        'journal': journal,
        'entries': journal.entries.all(),
    })
    return render(REQUEST, 'page.html', context)
def employment(REQUEST):
    journal = Journal.objects.get(journal_id=2)
    context.update({
        'blurb': 'A little about my work history.',
        'journal': journal,
        'entries': journal.entries.all(),
    })
    return render(REQUEST, 'page.html', context)
def education(REQUEST):
    journal = Journal.objects.get(journal_id=3)
    context.update({
        'blurb': 'A little about what I\'ve learned.',
        'journal': journal,
        'entries': journal.entries.all(),
    })
    return render(REQUEST, 'page.html', context)
def skills(REQUEST):
    journal = Journal.objects.get(journal_id=4)
    context.update({
        'blurb': 'A little about what I can do.',
        'journal': journal,
        'entries': journal.entries.all(),
    })
    return render(REQUEST, 'page.html', context)