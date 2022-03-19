from django.contrib import admin
from .models import utility, bio, work, edu, skills
# Register your models here.

admin.site.register(utility.Page)
admin.site.register(utility.Link)
admin.site.register(utility.Document)
admin.site.register(utility.Tag)

admin.site.register(bio.Story)

admin.site.register(work.Employer)
admin.site.register(work.Position)
admin.site.register(work.Duty)

admin.site.register(edu.Provider)
admin.site.register(edu.Course)
admin.site.register(edu.Certificate)

admin.site.register(skills.Skill)
