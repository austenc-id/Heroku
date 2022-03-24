from tabnanny import verbose
from django.db.models  import *
from random import randint
# Create your models here.

class Entry(Model):
    class Meta:
        verbose_name_plural = 'Entries'
    label = CharField(max_length=14)
    element_id = IntegerField(default=0)
    employer = CharField(max_length=48)
    start = DateField(blank=True)
    end = DateField(blank=True)
    positions = ManyToManyField('Position', blank=True, related_name='entry_positions')
    city = CharField(max_length=24)
    state = CharField(max_length=24)
    def __str__(self):
        return self.employer
    def dates(self):
        def format(date):
            if date.month == 1:
                month = 'Jan'
            if date.month == 2:
                month = 'Feb'
            if date.month == 3:
                month = 'Mar'
            if date.month == 4:
                month = 'Apr'
            if date.month == 5:
                month = 'May'
            if date.month == 6:
                month = 'Jun'
            if date.month == 7:
                month = 'Jul'
            if date.month == 8:
                month = 'Aug'
            if date.month == 9:
                month = 'Sep'
            if date.month == 10:
                month = 'Oct'
            if date.month == 11:
                month = 'Nov'
            if date.month == 12:
                month = 'Dec'
            return f'{month}. {date.day}, {date.year}'
        return f'{format(self.start)} - {format(self.end)}'
    def duration(self):
        if self.start != self.end:
            years = self.end.year - self.start.year
            months = (12 - self.end.month) + (12 - self.start.month)
            duration = ''
            if years > 0:
                duration += f'{years} years'
            if years > 0 and months > 0:
                duration += ' and'
            if months > 0:
                duration += f' {months} months'
            return duration
        return ''
    def location(self):
        return f'{self.city.title()}, {self.state.title()}'

class Position(Model):
    element_id = IntegerField(default=0)
    label = CharField(max_length=48)
    responsibilities = ManyToManyField('Responsibility', blank=True, related_name='position_responsibilities')
    def __str__(self):
        return self.label

class Responsibility(Model):
    class Meta:
        verbose_name_plural = 'Responsibilities'
    element_id = IntegerField(default=0)
    label = CharField(max_length=24)
    description = TextField()
    def __str__(self):
        return self.label