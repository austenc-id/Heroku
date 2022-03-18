from django.urls import path
from .views import index

app_name = 'bio'
urlpatterns = [
    path('', index, name='index')
]