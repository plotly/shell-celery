web: gunicorn app:server --log-file=-
default-worker: celery -A tasks worker --loglevel=info
beat-worker: celery -A tasks beat --loglevel=info