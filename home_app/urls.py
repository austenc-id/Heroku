from django.urls import path, include
from .views import *

app_name = 'home'
urlpatterns = [
    path('', index, name='index'),
    path('django', Django.index, name='django'),
    path('django/postgres', Django.postgres, name='dj_postgres'),
    path('django/heroku', Django.heroku, name='dj_heroku'),
]