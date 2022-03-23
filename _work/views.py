from django.shortcuts import render
from .models import *

# Create your views here.


def index(Request):
    context = {
        "pages": [
            {"label": "Bio", "url": "bio:index"},
            {"label": "Employment", "url": "bio:index"},
            {"label": "Education", "url": "bio:index"},
            {"label": "Skills", "url": "bio:index"},
        ],
        "active_page": "Employment",
    }
    return render(Request, "work.html", context)
