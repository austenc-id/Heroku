from multiprocessing import context
from django.shortcuts import render
from index.pages import pages

def index(Request):
    context = {
        'pages': pages,
        'active_page': 'Home',

    }
    return render(Request, 'home.html', context)
