web: python manage.py makemigrations; python manage.py migrate; gunicorn WiWeb.wsgi --log-file -
celery: celery worker --app=WiWeb.celery.app --concurrency=1