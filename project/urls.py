from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("_home.urls")),
    path("bio/", include("_bio.urls")),
    path("work/", include("_work.urls")),
]
