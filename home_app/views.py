from django.shortcuts import render

def index(Request):
    return render(Request, 'pages/home.html')

class Django:

    def index(Request):
        return render(Request, 'pages/django.html')

    def postgres(Request):
        return render(Request, 'pages/django/postgres.html')

    def heroku(Request):
        return render(Request, 'pages/django/heroku.html')