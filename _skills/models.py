from django.db.models import *

# Create your models here.
class Category(Model):
    class Meta:
        verbose_name_plural = 'Categories'
    label = CharField(max_length=48)
    blurb = TextField()
    skills = ManyToManyField('Skill', blank=True,
                                related_name='category_skills')
    def __str__(self):
        return self.label

class Skill(Model):
    label = CharField(max_length=48)
    rank = IntegerField(default=0)
    def __str__(self):
        return self.label