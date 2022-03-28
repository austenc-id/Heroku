from django.db.models import *

# Create your models here.

class Story(Model):
    class Meta:
        verbose_name_plural = 'Stories'
    title = CharField(max_length=14)
    content = TextField()
    def __str__(self):
        return self.title