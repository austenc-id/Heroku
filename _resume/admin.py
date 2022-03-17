from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Journal)
admin.site.register(Entry)
admin.site.register(Position)
admin.site.register(Program)
admin.site.register(Certificate)