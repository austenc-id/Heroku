from django.db.models import *
from datetime import datetime
# Create your models here.

class Journal(Model):
    class Meta:
        verbose_name = '1. Journal'
    journal_id = IntegerField()
    label = CharField(max_length=12)
    list_label = CharField(max_length=12, blank=True)
    entries = ManyToManyField('Entry', related_name='journal_entries')
    def __str__(self):
        return self.label

class Entry(Model):
    class Meta:
        verbose_name = '2. Entry'
        verbose_name_plural = '2. Entries'
    label = CharField(max_length=48)
    blurb = TextField(blank=True)
    start = DateField(default='2022-03-16', blank=True, null=True)
    end = DateField(default='2022-03-16', blank=True, null=True)
    positions = ManyToManyField('Position', related_name='entry_positions', blank=True, null=True)
    programs = ManyToManyField('Program', related_name='entry_programs', blank=True, null=True)
    def __str__(self):
        return self.label

class Position(Model):
    class Meta:
        verbose_name = '3a. Position'
    label = CharField(max_length=48, blank=True)
    employer = CharField(max_length=48, blank=True)
    street = CharField(max_length=48, blank=True)
    city = CharField(max_length=24, blank=True)
    state = CharField(max_length=24, blank=True)
    start = DateField(default='2022-03-16')
    end = DateField(default='2022-03-16')
    def __str__(self):
        return self.label
    def address(self):
        return f'{self.street}, {self.city}, {self.state}'
    def location(self):
        return f'{self.city}, {self.state}'

class Program(Model):
    class Meta:
        verbose_name = '3b. Program'
    label = CharField(max_length=48, blank=True)
    provider = CharField(max_length=48, blank=True)
    street = CharField(max_length=48, blank=True)
    city = CharField(max_length=24, blank=True)
    state = CharField(max_length=24, blank=True)
    start = DateField(default='2022-03-16')
    end = DateField(default='2022-03-16')
    certificates = ManyToManyField('Certificate', related_name='program_certs', blank=True, null=True)
    def __str__(self):
        return self.label
    def address(self):
        return f'{self.street}, {self.city}, {self.state}'
    def location(self):
        return f'{self.city}, {self.state}'

class Certificate(Model):
    class Meta:
        verbose_name = '4b. Certificate'
    label = CharField(max_length=48)
    provider = CharField(max_length=48)
    earned = DateField(default='2022-03-16')
    expiration = DateField(default='2022-03-16', blank=True, null=True)
    def __str__(self):
        return self.label