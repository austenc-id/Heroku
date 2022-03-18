from django.db.models import *

# Create your models here.
class Employer(Model):
    label = CharField(max_length=14)
    link = URLField()
    blurb = TextField()
    start = DateField()
    end = DateField()
    city = CharField(max_length=16, blank=True)
    state = CharField(max_length=16, blank=True)
    state_code = CharField(max_length=2, blank=True)
    positions = ManyToManyField('Position', blank=True,
                            related_name='employer_positions')
    def __str__(self):
        return self.label

class Position(Model):
    label = CharField(max_length=48)
    link = URLField()
    blurb = CharField(max_length=16)
    start = DateField()
    end = DateField()
    duties = ManyToManyField('Duty', blank=True,
                                related_name='position_duties')
    def __str__(self):
        return self.label

class Duty(Model):
    class Meta:
        verbose_name_plural = 'Duties'
    label = CharField(max_length=16)
    def __str__(self):
        return self.label