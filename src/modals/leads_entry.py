from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class WebLeadsEntry(BaseModel):
    id: str
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    service: Optional[str] = None
    budget: Optional[str] = None
    goal: Optional[str] = None
    createdAt: Optional[datetime] = None
    
class LeadsEntry(BaseModel):
    id: str
    client_name: str
    request_type: str
    proposal_status: Optional[str] = None
    work_status: Optional[str] = None
    currency: Optional[str] = None
    fees: Optional[float] = None
    payment_status: Optional[str] = None
    linkedin_url: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None