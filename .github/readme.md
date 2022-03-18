# Django Build

## To Do

> Tasks that need to get done.

- Add additional fields to models.
- Prepare for project deployment.
        - Reinit project without database.
- Deploy

## Project Code

> Meant to make it easier to compare code cross-app.
>
> Last update: 17-MAR-2022 20:00

### Models

<ul><details>
    <summary>_home</summary>
<ul><details>
    <summary>Link</summary>
    <ul><h3>Defines relevant urls to external websites.<h3></ul>

```python
 class Link(Model):
    label = CharField(max_length=48)
    url = URLField()
    def __str__(self):
        return self.label
```
</details></ul>
<ul><details>
    <summary>Page</summary>
    <ul><h3>One page for each app.<h3></ul>

```python
class Page(Model):
    label = CharField(max_length=24)
    url = CharField(max_length=24)
    blurb = TextField()
    def __str__(self):
        return self.label
```
</details></ul>
<ul><details>
    <summary>Document</summary>
    <ul><h3>Documents than can be made available for download.<h3></ul>

```python
class Document(Model):
    label = CharField(max_length=48)
    file = FileField(upload_to='documents')
    def __str__(self):
        return self.label
```
</details></ul>
</details></ul>

<ul><details>
    <summary>_bio</summary>
<ul><details>
    <summary>Entry</summary>
    <ul><h3>Short stories.<h3></ul>

```python
class Entry(Model):
    class Meta:
        verbose_name_plural = 'Entries'
    label = CharField(max_length=14)
    blurb = TextField()
    def __str__(self):
        return self.label
```
</details></ul>
</details></ul>

<ul><details>
    <summary>_employment</summary>
<ul><details>
    <summary>Employer</summary>
    <ul><h3>Description.<h3></ul>

```python
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
```
</details></ul>
<ul><details>
    <summary>Position</summary>
    <ul><h3>Description.<h3></ul>

```python
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
```
</details></ul>
<ul><details>
    <summary>Duty</summary>
    <ul><h3>Description.<h3></ul>

```python
class Duty(Model):
    class Meta:
        verbose_name_plural = 'Duties'
    label = CharField(max_length=16)
    def __str__(self):
        return self.label
```
</details></ul>
</details></ul>

<ul><details>
    <summary>_education</summary>
<ul><details>
    <summary>Category</summary>
    <ul><h3>Description.<h3></ul>

```python
class Category(Model):
    class Meta:
        verbose_name_plural = 'Categories'
    label = CharField(max_length=48)
    blurb = TextField()
    courses = ManyToManyField('Course', blank=True,
                                related_name='category_courses')
    def __str__(self):
        return self.label
```
</details></ul>
<ul><details>
    <summary>Course</summary>
    <ul><h3>Description.<h3></ul>

```python
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
```
</details></ul>
<ul><details>
    <summary>Certificate</summary>
    <ul><h3>Description.<h3></ul>

```python
class Certificate(Model):
    label = CharField(max_length=48)
    provider = ForeignKey('Provider', null=True, on_delete=SET_NULL,
                                related_name='course_provider')
    link = URLField()
    effective = DateField()
    expires = DateField()
    document = FileField(upload_to='documents/certificates', blank=True)
    def __str__(self):
        return self.label
```
</details></ul>
<ul><details>
    <summary>Provider</summary>
    <ul><h3>Description.<h3></ul>

```python
class Provider(Model):
    label = CharField(max_length=48)
    def __str__(self):
        return self.label
```
</details></ul>
</details></ul>

<ul><details>
    <summary>_skills</summary>
<ul><details>
    <summary>Category</summary>
    <ul><h3>Description.<h3></ul>

```python
class Category(Model):
    class Meta:
        verbose_name_plural = 'Categories'
    label = CharField(max_length=48)
    blurb = TextField()
    skills = ManyToManyField('Skill', blank=True,
                                related_name='category_skills')
    def __str__(self):
        return self.label
```
</details></ul>
<ul><details>
    <summary>Skill</summary>
    <ul><h3>Description.<h3></ul>

```python
class Skill(Model):
    label = CharField(max_length=48)
    rank = IntegerField(default=0)
    def __str__(self):
        return self.label
```
</details></ul>
</details></ul>

### Views

<ul><details>
    <summary>_home</summary>

```python
def index(Request):
    context = {
        'links': Link.objects.all(),
        'pages': Page.objects.all(),
        'page': Page.objects.get(label='home')
    }
    return render(Request, 'pages/home.html', context)
```
</details></ul>

<ul><details>
    <summary>_bio</summary>

```python
def index(Request):
    context = {
        'links': Link.objects.all(),
        'pages': Page.objects.all(),
        'page': Page.objects.get(label='bio'),
        'entries': Entry.objects.all()
    }
    return render(Request, 'pages/bio.html', context)
```
</details></ul>

<ul><details>
    <summary>_employment</summary>

```python
def index(Request):
    context = {
        'links': Link.objects.all(),
        'pages': Page.objects.all(),
        'page': Page.objects.get(label='employment'),
        'employers': Employer.objects.all()
    }
    return render(Request, 'pages/work.html', context)
```
</details></ul>

<ul><details>
    <summary>_education</summary>

```python
def index(Request):
    context = {
        'links': Link.objects.all(),
        'pages': Page.objects.all(),
        'page': Page.objects.get(label='education'),
        'categories': Category.objects.all()
    }
    return render(Request, 'pages/edu.html', context)
```
</details></ul>

<ul><details>
    <summary>_skills</summary>

```python
def index(Request):
    context = {
        'links': Link.objects.all(),
        'pages': Page.objects.all(),
        'page': Page.objects.get(label='skills'),
        'categories': Category.objects.all(),
    }
    return render(Request, 'pages/skills.html', context)
```
</details></ul>
