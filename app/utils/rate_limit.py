from time import time
from fastapi import HTTPException

rate_store = {}

def rate_limit(key: str, limit: int, per_seconds: int):
    now = time()
    bucket = rate_store.get(key, [])
    bucket = [t for t in bucket if t > now - per_seconds]
    if len(bucket) >= limit:
        raise HTTPException(status_code=429, detail="Too many requests")
    bucket.append(now)
    rate_store[key] = bucket
