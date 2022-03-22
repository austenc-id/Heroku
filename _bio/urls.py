from django.urls import path
from .views import *

app_name = 'bio'
urlpatterns = [
    path('', index, name='index'),
    path('<str:story>/', story, name='story'),
]