from django.contrib import admin
from .models import Employer, Position, Category
# Register your models here.

admin.site.register(Employer)
admin.site.register(Position)
admin.site.register(Category)
