import duckdb
from threading import Lock

DB_PATH = "pulse.db"
_lock = Lock()

def get_conn():
    return duckdb.connect(DB_PATH)

def execute(query, params=None):
    with _lock:
        conn = get_conn()
        if params:
            conn.execute(query, params)
        else:
            conn.execute(query)
        conn.close()
