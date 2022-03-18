from django.db.models import ( Model, CharField, TextField, ManyToManyField,
                                URLField, DateField, BooleanField, FileField,
                                ForeignKey, SET_NULL )

class Provider(Model):
    label = CharField(max_length=48)
    blurb = TextField()
    courses = ManyToManyField('Course', blank=True, related_name='provider_courses')
    city = CharField(max_length=16, blank=True)
    state = CharField(max_length=16, blank=True)
    state_code = CharField(max_length=2, blank=True)
    def __str__(self):
        return self.label

class Course(Model):
    label = CharField(max_length=48)
    link = URLField()
    start = DateField()
    end = DateField()
    graduated = BooleanField(default=False)
    certificates = ManyToManyField('Certificate', blank=True, related_name='course_certs')
    def __str__(self):
        return self.label

class Certificate(Model):
    label = CharField(max_length=48)
    provider = ForeignKey('Provider', null=True, on_delete=SET_NULL, related_name='cert_provider')
    link = URLField()
    effective = DateField()
    expires = DateField()
    document = FileField(upload_to='documents/certificates', blank=True)
    def __str__(self):
        return self.label
