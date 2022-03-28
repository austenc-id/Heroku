from django.db.models import *
from project.utils import format
# Create your models here.

class Group(Model):
    group_id = IntegerField()
    label = CharField(max_length=14)
    courses = ManyToManyField('Course', blank=True, related_name='group_courses')
    def __str__(self):
        return self.label

class Course(Model):
    element_id = CharField(default='0', max_length=3)
    label = CharField(max_length=14)
    name = CharField(max_length=36)
    provider = CharField(max_length=36)
    start = CharField(max_length=18)
    end = CharField(max_length=18)
    def __str__(self):
        return self.provider
    def dates(self):
        start = format.dates(self.start)
        end = format.dates(self.end)
        if start != None and end != None:
            return f'{start} - {end}'
        elif start == None and end != None:
            return f'{self.start} - {end}'
        elif start != None and end == None:
            return f'{start} - {self.end}'
        return f'{self.start} - {self.end}'