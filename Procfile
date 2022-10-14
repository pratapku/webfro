release: python manage.py migrate
web: daphne sowe.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A sowe.celery worker -l info
celerybeat: celery -A sowe beat -l INFO 
celeryworker2: celery -A sowe.celery worker & celery -A sowe beat -l INFO & wait -n