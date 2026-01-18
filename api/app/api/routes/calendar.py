from fastapi import APIRouter, HTTPException, Query
from datetime import datetime, timedelta
from typing import List, Optional
import logging

from app.services.calendar_service import CalendarService
from app.schemas.calendar import (
    AppointmentCreate,
    AppointmentResponse,
    AvailableSlotsResponse
)

logger = logging.getLogger(__name__)
router = APIRouter()
calendar_service = CalendarService()


@router.get("/available-slots", response_model=AvailableSlotsResponse)
async def get_available_slots(
    date: str = Query(..., description="Data no formato YYYY-MM-DD"),
    duration: int = Query(60, description="Duração em minutos")
):
    """
    Retorna horários disponíveis para um dia específico
    """
    try:
        slots = await calendar_service.get_available_slots(date, duration)
        return slots
    except Exception as e:
        logger.error(f"Error getting available slots: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/appointments", response_model=AppointmentResponse, status_code=201)
async def create_appointment(appointment: AppointmentCreate):
    """
    Cria um novo agendamento no Google Calendar
    """
    try:
        result = await calendar_service.create_appointment(appointment)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error creating appointment: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/appointments")
async def get_appointments(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
):
    """
    Lista todos os agendamentos
    """
    try:
        appointments = await calendar_service.get_appointments(start_date, end_date)
        return appointments
    except Exception as e:
        logger.error(f"Error getting appointments: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/appointments/{event_id}")
async def cancel_appointment(event_id: str):
    """
    Cancela um agendamento
    """
    try:
        await calendar_service.cancel_appointment(event_id)
        return {"message": "Appointment cancelled successfully"}
    except Exception as e:
        logger.error(f"Error cancelling appointment: {e}")
        raise HTTPException(status_code=500, detail=str(e))
