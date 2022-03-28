from django.shortcuts import render
from project.pages import pages

def index(Request):
    context = {
        'pages': pages,
        'active_page': 'Home',

    }
    return render(Request, 'home.html', context)