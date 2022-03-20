from multiprocessing import context
from django.shortcuts import render

def index(Request):
    context = {
        'page': 'Home',

    }
    return render(Request, 'home.html', context)