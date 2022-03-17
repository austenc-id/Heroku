from django.urls import path, include
from .views import *

app_name = 'resume'
urlpatterns = [
    path('bio', bio, name='bio'),
    path('employment', employment, name='employment'),
    path('education', education, name='education'),
    path('skills', skills, name='skills'),
]