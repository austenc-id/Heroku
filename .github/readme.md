1. create directory
2. run bash
    - ```python -m venv env```
    - ```source env/scripts/activate```
    - ```pip install django django-heroku gunicorn```
    - ```pip freeze > requirements.txt```
    - ```git init```
    - ```touch Procfile runtime.txt app.json```
    - ```django-admin startproject <project_name> .```
    - ```mkdir assets assets/templates assets/style assets/scripts assets/images/ assets/images/icons/```
    - ```touch assets/templates/base.html assets/templates/index.html assets/style/theme.css assets/style/bootstrap.css assets/style/bootstrap.css.map <project_name>/views.py .gitignore```
    - ```django-admin startapp <app_name>```
3. open assets/templates/base.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Austen C. Myers</title>
    <!-- Tab Icon" -->
    <link rel="shortcut icon" href="{% static 'images/icons/site-tab.png' %}">
    <!-- Bootstrap -->
    <link rel="stylesheet" href="{% static 'style/bootstrap.css' %}">
    <!-- CSS -->
    <link rel="stylesheet" href="{% static 'style/theme.css' %}">
</head>

<body class="bg-void container p-4">
    {% block index %}{% endblock index %}
</body>

</html>
```
4. open assets/templates/index.html
```html
{% extends 'base.html' %}
{% block index %}
{% endblock index %}
```
5. open project/urls.py
```python
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
    # path('', include('<app_name>.urls))
]
```
6. open project/views.py
```python
from django.shortcuts import render

def index(Request):
    return render(Request, 'index.html')
```
7. run psql terminal
    - enter psql password
    - ```CREATE DATABASE <project_name>;```
    - ```\c <project_name>;```
8. open _project/settings.py
    ```python
    DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': '<project_name>',
                'USER': 'postgres',
                'PASSWORD': '<password>',
                'HOST': 'localhost',
                'PORT': '4000',
            }
        }
    INSTALLED_APPS.append('<app_name>')
    STATICFILES_DIRS = [BASE_DIR / 'assets']
    STATIC_ROOT = BASE_DIR / 'staticroot'
    TEMPLATES[0].update({'DIRS':[ BASE_DIR / 'assets/templates']})
    ```
9. open .gitignore
    ```
    env
    __pycache__
    migrations
    ```
10. run bash
    - ```djmake```
    - ```djmigrate```
    - ```djsuper```
    - ```djserve```
    - ```heroku create <app_name>```
        - if heroku app not in .git/config:
        - ``` heroku git:remote --app <app_name>```
11. open runtime.txt
    - ```python-<version>```
12. open Procfile
    - ```web: gunicorn <project_name>.wsgi```
13. open app.json
```json
{
  "name": "Start on Heroku: Python",
  "description": "A barebones Python app, which can easily be deployed to Heroku.",
  "image": "heroku/python",
  "repository": "https://github.com/heroku/python-getting-started",
  "keywords": ["python", "django" ],
  "addons": [ "heroku-postgresql" ],
  "env": {
    "SECRET_KEY": {
      "description": "The secret key for the Django application.",
      "generator": "secret"
    }
  },
  "environments": {
    "test": {
      "scripts": {
        "test-setup": "python manage.py collectstatic --noinput",
        "test": "python manage.py test"
      }
    }
  }
}
```
14. open _project/settings.py
    ```python
    import django_heroku

    ALLOWED_HOSTS = [
        '<heroku_app_name>.herokuapp.com'
    ]

    django_heroku.settings(locals())
    ```
15. git commit
16. figure out SECRET_KEY
17. run bash
    - ```git push heroku main```
    - or
    - ```git push heroku <branch_name>:main```
    - then
    - ```heroku ps:scale web=1```
