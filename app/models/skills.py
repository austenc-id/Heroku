from django.db.models import (Model, CharField, IntegerField, ManyToManyField)
from .utility import Tag

class Skill(Model):
    label = CharField(max_length=48)
    rank = IntegerField(default=0)
    tags = ManyToManyField(Tag, blank=True, related_name='skill_tags')
    def __str__(self):
        return self.label