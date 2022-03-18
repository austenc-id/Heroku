from django.db.models  import *

# Create your models here.
class Link(Model):
    label = CharField(max_length=48)
    url = URLField()
    def __str__(self):
        return self.label

class Page(Model):
    label = CharField(max_length=24)
    url = CharField(max_length=24)
    blurb = TextField()
    def __str__(self):
        return self.label

class Document(Model):
    label = CharField(max_length=48)
    file = FileField(upload_to='documents')
    def __str__(self):
        return self.label