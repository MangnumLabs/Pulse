import redis
import time

def get_redis():
    while True:
        try:
            r = redis.Redis(host="redis", port=6379, decode_responses=True)
            r.ping()
            return r
        except redis.exceptions.ConnectionError:
            print("Waiting for Redis...")
            time.sleep(2)

r = get_redis()

def pop_event():
    event_id = r.rpop("pulse:events")
    print(event_id)
    if event_id is None:
        return None
    return event_id
