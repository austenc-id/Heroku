from django.urls import path
from .views import *

app_name = 'edu'
urlpatterns = [
    path('', index, name='index'),
    path('<str:group>/', group, name='group'),
]