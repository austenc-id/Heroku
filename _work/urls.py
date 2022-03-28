from django.urls import path
from .views import *

app_name = "work"
urlpatterns = [
    path("", index, name="index"),
    path('<str:entry>/', details, name='details'),
]