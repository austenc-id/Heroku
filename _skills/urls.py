from django.urls import path
from .views import index

app_name = 'skills'
urlpatterns = [
    path('', index, name='index')
]