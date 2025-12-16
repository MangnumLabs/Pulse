from fastapi import FastAPI
from app.routes.events import router as events
from app.db import execute


def init_db():
    query = """
    CREATE TABLE IF NOT EXISTS events (
        event_id        INTEGER,
        type            VARCHAR NOT NULL,
        status          VARCHAR NOT NULL,
        s3_bucket       VARCHAR NOT NULL,
        s3_key          VARCHAR NOT NULL,
        payload_size    INTEGER,
        created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at      TIMESTAMP
    );
    """
    execute(query)




app = FastAPI(title="Pulse")
app.include_router(events)


@app.on_event("startup")
def startup():
    init_db()
