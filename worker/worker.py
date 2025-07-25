from celery import Celery
from datetime import datetime
import time
import os

redis_host = os.getenv("REDIS_HOST", "redis")
broker_url = f"redis://{redis_host}:6379/0"

app = Celery("worker", broker=broker_url)

@app.task
def process_job(job_id: int, enqueued_time: str):
    print(f"Processing job {job_id} queued at {enqueued_time}")
    start = datetime.now()
    time.sleep(5)
    end = datetime.now()
    print(f"Finished job {job_id} queued at {enqueued_time} - {start} - {end} = {end-start}")
