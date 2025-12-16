from .queue import pop_event
from .db import fetch_event, update_status
from .s3 import read_payload

def main():
    print("Worker started...")
    while True:
        print("------ Loop start-------")
        event_id = pop_event()
        if event_id is None:
            print("---Lopp")
            continue
        print(f"Processing event {event_id}")

        update_status(event_id, "processing")

        event = fetch_event(event_id)
        payload = read_payload(event[3], event[4])  # bucket, key

        # ---- PROCESS EVENT HERE ----
        print("Payload:", payload)

        update_status(event_id, "done")
        print(f"Event {event_id} done")
        print("-----Loop Ended------")

if __name__ == "__main__":
    main()
