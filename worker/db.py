import duckdb
from threading import Lock

DB_PATH = "pulse.db"
_lock = Lock()

def fetch_event(event_id: int):
    conn = duckdb.connect(DB_PATH)
    row = conn.execute(
        "SELECT * FROM events WHERE id = ?",
        [event_id]
    ).fetchone()
    conn.close()
    return row

def update_status(event_id: int, status: str):
    with _lock:
        conn = duckdb.connect(DB_PATH)
        conn.execute(
            """
            UPDATE events
            SET status = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            [status, event_id]
        )
        conn.close()
