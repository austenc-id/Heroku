from django.shortcuts import render
from _resume.models import Journal, Entry

def home(data):
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
        'sections': Journal.objects.all(),
        'page': 'home',
        'blurb': 'Welcome. Have a look around.'
    }
    return render(data, 'home.html', context)