from django.db.models import *

# Create your models here.

class Category(Model):
    class Meta:
        verbose_name_plural = 'Categories'
    label = CharField(max_length=48)
    blurb = TextField()
    courses = ManyToManyField('Course', blank=True,
                                related_name='category_courses')
    def __str__(self):
        return self.label

class Course(Model):
    label = CharField(max_length=48)
    provider = ForeignKey('Provider', null=True, on_delete=SET_NULL,
                                related_name='course_provider')
    link = URLField()
    start = DateField()
    end = DateField()
    graduated = BooleanField(default=False)
    certificates = ManyToManyField('Certificate', blank=True,
                                    related_name='course_certs')
    city = CharField(max_length=16, blank=True)
    state = CharField(max_length=16, blank=True)
    state_code = CharField(max_length=2, blank=True)
    def __str__(self):
        return self.label

class Certificate(Model):
    label = CharField(max_length=48)
    provider = ForeignKey('Provider', null=True, on_delete=SET_NULL,
                                related_name='cert_provider')
    link = URLField()
    effective = DateField()
    expires = DateField()
    document = FileField(upload_to='documents/certificates', blank=True)
    def __str__(self):
        return self.label
