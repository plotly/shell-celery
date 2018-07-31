import datetime
import json
import time
import numpy as np
import os
import pandas as pd
import plotly
import redis

from celery import Celery

celery_app = Celery("Celery App", broker=os.environ["REDIS_URL"])

redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])

REDIS_HASH_NAME = os.environ.get("DASH_APP_NAME", "app-data")
REDIS_KEYS = {"DATASET": "DATASET", "DATE_UPDATED": "DATE_UPDATED"}

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    print("----> setup_periodic_tasks")
    sender.add_periodic_task(
        5,  # seconds
        # an alternative to the @app.task decorator:
        # wrap the function in the app.task function
        update_data.s(),
        name="Update data",
    )


@celery_app.task
def update_data():
    print('pull new data')
    data = np.random.normal(size=1)
    print(data[0])
    redis_instance.hset(
        REDIS_HASH_NAME,
        REDIS_KEYS["DATASET"],
        data[0],
    )