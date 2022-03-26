from django.db.models  import *
from random import randint
from project.utils import format, calculate as calc
# Create your models here.
class Entry(Model):
    class Meta:
        verbose_name_plural = 'Entries'
    label = CharField(max_length=18)
    element_id = IntegerField(default=0)
    employer = CharField(max_length=48)
    start = CharField(max_length=18, blank=True)
    end = CharField(max_length=18, blank=True)
    positions = ManyToManyField('Position', blank=True, related_name='entry_positions')
    city = CharField(max_length=24)
    state = CharField(max_length=24)
    def __str__(self):
        return self.employer
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
    def duration(self):
        duration = calc.dates(self.start, self.end)
        if duration != (0, 0, 0):
            years = duration[0]
            months = duration[1]
            return f'{years} years & {months} months'
        return ''
    def location(self):
        return f'{self.city.title()}, {self.state.title()}'

class Position(Model):
    element_id = IntegerField(default=0)
    label = CharField(max_length=48)
    start = CharField(max_length=18, blank=True)
    end = CharField(max_length=18, blank=True)
    duties = ManyToManyField('Duty', blank=True, related_name='position_duties')
    def __str__(self):
        return self.label

class Duty(Model):
    class Meta:
        verbose_name_plural = 'Duties'
    element_id = IntegerField(default=0)
    label = CharField(max_length=24)
    description = TextField()
    def __str__(self):
        return self.label