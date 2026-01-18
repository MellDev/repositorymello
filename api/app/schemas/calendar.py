from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class AppointmentCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    service: str
    date: str
    time: str
    message: Optional[str] = None


class AppointmentResponse(BaseModel):
    message: str
    appointment: dict


class AvailableSlotsResponse(BaseModel):
    date: str
    available_slots: List[str]
    duration: int
    timezone: str = "America/Sao_Paulo"
