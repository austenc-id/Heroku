"""_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # app_name = 'home'
    path('', include('_home.urls')),
    # app_name = 'bio'
    path('bio', include('_bio.urls')),
    # app_name = 'work'
    path('employment', include('_employment.urls')),
    # app_name = 'edu'
    path('education', include('_education.urls')),
    # app_name = 'skills'
    path('skills', include('_skills.urls')),
]
