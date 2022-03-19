1. create directory
2. run bash
    - ```djheroenv```
    - ```djheroinit```
    - ```djheroproj```
5. run psql terminal
    - enter psql password
    - ```CREATE DATABASE <project_name>;```
    - ```\c <project_name>;```
6. open _project/settings.py
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
    ```
7. run bash
    - ```djmake```
    - ```djmigrate```
    - ```djserve```