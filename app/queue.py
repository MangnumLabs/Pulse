import redis
import json

r = redis.Redis(host="redis", port="6379", decode_responses=True)

def push_event(event_id:int , payload:dict):
    r.lpush("pulse_events", json.dumps({
        "event_id": event_id,
        "payload": payload
    }))