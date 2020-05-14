release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn LMS.wsgi --log-file -
