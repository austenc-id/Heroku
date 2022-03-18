from django.db.models import *

# Create your models here.

class Entry(Model):
    class Meta:
        verbose_name_plural = 'Entries'
    label = CharField(max_length=14)
    blurb = TextField()
    def __str__(self):
        return self.label