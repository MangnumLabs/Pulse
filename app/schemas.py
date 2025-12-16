from pydantic import BaseModel
from typing import Dict, Any

class EventCreate(BaseModel):
    id: int
    type: str
    payload: Dict[str, Any]
