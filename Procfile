#web: gunicorn myproject.wsgi
#celery: celery -A myproject worker -l INFO
#celery: celery -A myproject beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
#web: daphne myproject.asgi:application --port $PORT --bind 0.0.0.0 -v2
####git commit -m "first commit"  git push -u origin123 main
#release: python manage.py migrate
web: daphne  myproject.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A  myproject.celery worker -l info
celerybeat: celery -A  myproject beat -l INFO 
celeryworker2: celery -A  myproject worker & celery -A  myproject -l INFO & wait -n
