1. create directory
2. run bash
    - ```djheroenv```
    - ```djheroinit```
    - ```djheroproj```
3. run psql terminal
    - enter psql password
    - ```CREATE DATABASE <project_name>;```
    - ```\c <project_name>;```
4. open _project/settings.py
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
    STATICFILES_DIRS = [BASE_DIR / '_assets']
    STATIC_ROOT = BASE_DIR / 'staticroot'
    TEMPLATES[0].update({'DIRS':[ BASE_DIR / '_assets/templates']})
    ```
5. open .gitignore
    ```
    env
    __pycache__
    migrations
    _assets
    ```
6. run bash
    - ```djmake```
    - ```djmigrate```
    - ```djserve```
    - ```heroku create <app_name>```
7. open runtime.txt
    - ```python-<version>```
8. open Procfile
    - ```web: gunicorn _project.wsgi```
9. open _project/settings.py
    ```python
    import django_heroku

    ALLOWED_HOSTS = [
        '<heroku_app_name>.herokuapp.com'
    ]

    django_heroku.settings(locals())
    ```
10. git commit
11. figure out SECRET_KEY
12. run bash
    - ```git push heroku main```
    - or
    - ```git push heroku <branch_name>:main```
    - then
    - ```heroku ps:scale web=1```
