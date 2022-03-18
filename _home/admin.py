from django.contrib import admin
from .models import Link, Page, Document

# Register your models here.
admin.site.register(Link)
admin.site.register(Page)
admin.site.register(Document)