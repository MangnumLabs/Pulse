from fastapi import APIRouter
from app.db import get_conn
from app.queue import push_event
from app.schemas import EventCreate
from app.s3 import upload_payload, BUCKET

router = APIRouter(prefix="/events")

@router.post("")
def create_event(event: EventCreate):
    conn = get_conn()

    result = conn.execute(
        """
        INSERT INTO events (event_id, type, status, s3_bucket, s3_key, payload_size)
        VALUES (?, ?, ?, ?, ?, ?)
        RETURNING event_id
        """,
        [event.id, event.type, "pending", BUCKET, "", 0]
    ).fetchone()

    event_id = result[0]

    s3_key, size = upload_payload(event.id, event.payload)

    conn.execute(
        """
        UPDATE events
        SET s3_key = ?, payload_size = ?
        WHERE event_id = ?
        """,
        [s3_key, size, event_id]
    )

    conn.close()

    push_event(event_id, event.payload)

    return {"id": event_id, "status": "queued"}
