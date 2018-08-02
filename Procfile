web: gunicorn app:server --log-file=-
beat: celery -A tasks beat --loglevel=info
worker: celery -A tasks worker --loglevel=info