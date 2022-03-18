from django.db.models import (Model, CharField, TextField)

class Story(Model):
    class Meta:
        verbose_name_plural = 'Stories'
    label = CharField(max_length=14)
    blurb = TextField()
    def __str__(self):
        return self.label