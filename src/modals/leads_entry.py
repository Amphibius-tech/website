from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class LeadsEntry(BaseModel):
    id: str
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    service: Optional[str] = None
    budget: Optional[str] = None
    goal: Optional[str] = None
    createdAt: Optional[datetime] = None