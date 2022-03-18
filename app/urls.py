from django.urls import path
from .views import *

app_name = 'site'
urlpatterns = [
    path('', home, name='home'),
    path('bio', bio, name='bio'),
    path('work', work, name='work'),
    path('edu', edu, name='edu'),
    path('skills', skills, name='skills'),
]