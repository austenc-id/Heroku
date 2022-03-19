from multiprocessing import context
from django.shortcuts import render

def index(Request):
    context = {
        'page': 'home',

    }
    return render(Request, 'home.html', context)