from fastapi import FastAPI
from redis import Redis
from datetime import datetime
import os

from worker import process_job

app = FastAPI()
redis_host = os.getenv("REDIS_HOST", "redis")
redis = Redis(host=redis_host, port=6379, decode_responses=True)

QUEUE_NAME = "jobs"

job_id = 0 

@app.post("/job")
def create_job():
    global job_id
    job_id += 1
    now = datetime.now().isoformat()
    process_job.delay(job_id, now)
    print(f"[{now}] Job sent to Celery queue with id {job_id}")
    return {"status": "queued", "time": now, "job_id": job_id}
