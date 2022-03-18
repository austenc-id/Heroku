from django.urls import path
from .views import index

app_name = 'work'
urlpatterns = [
    path('', index, name='index')
]