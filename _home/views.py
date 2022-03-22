from multiprocessing import context
from django.shortcuts import render

def index(Request):
    context = {
        'pages': [
            {'label': 'Bio', 'url': 'bio:index'},
            {'label': 'Employment', 'url': 'bio:index'},
            {'label': 'Education', 'url': 'bio:index'},
            {'label': 'Skills', 'url': 'bio:index'},
        ],
        'active_page': 'Home',

    }
    return render(Request, 'home.html', context)