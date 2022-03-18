from django.contrib import admin
from .models import Category, Course, Certificate
# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Certificate)