web: gunicorn app:server --log-file=-
worker: celery -A tasks worker --beat --loglevel=info