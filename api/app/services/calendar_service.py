from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from typing import List
import logging
import os

from app.config import settings
from app.schemas.calendar import AppointmentCreate, AvailableSlotsResponse

logger = logging.getLogger(__name__)


class CalendarService:
    def __init__(self):
        self.calendar_id = settings.google_calendar_id
        self.service = None
        self._initialize_service()

    def _initialize_service(self):
        """Inicializa o serviço do Google Calendar"""
        try:
            if not os.path.exists(settings.google_service_account_file):
                logger.warning("Google Calendar credentials not found")
                return

            credentials = service_account.Credentials.from_service_account_file(
                settings.google_service_account_file,
                scopes=['https://www.googleapis.com/auth/calendar']
            )
            self.service = build('calendar', 'v3', credentials=credentials)
            logger.info("✅ Google Calendar service initialized")
        except Exception as e:
            logger.error(f"Failed to initialize Google Calendar: {e}")

    async def get_available_slots(self, date_str: str, duration: int = 60) -> AvailableSlotsResponse:
        """Retorna horários disponíveis para um dia"""
        if not self.service:
            # Retornar slots mockados se não tiver credenciais
            return await self._get_mock_slots(date_str, duration)

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            day_of_week = date.weekday()

            # Domingo não trabalha
            if day_of_week == 6:
                return AvailableSlotsResponse(
                    date=date_str,
                    available_slots=[],
                    duration=duration
                )

            # Define horário de término (Sábado até 13h, outros dias até 18h)
            end_hour = 13 if day_of_week == 5 else 18

            # Buscar eventos do dia
            time_min = date.replace(hour=0, minute=0, second=0).isoformat() + 'Z'
            time_max = date.replace(hour=23, minute=59, second=59).isoformat() + 'Z'

            events_result = self.service.events().list(
                calendarId=self.calendar_id,
                timeMin=time_min,
                timeMax=time_max,
                singleEvents=True,
                orderBy='startTime'
            ).execute()

            events = events_result.get('items', [])

            # Gerar todos os slots possíveis (9h às 18h ou 13h)
            all_slots = []
            for hour in range(9, end_hour):
                all_slots.append(f"{hour:02d}:00")
                if hour < end_hour - 1 or (hour == end_hour - 1 and duration <= 30):
                    all_slots.append(f"{hour:02d}:30")

            # Filtrar slots ocupados
            busy_slots = []
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                if 'T' in start:
                    start_time = datetime.fromisoformat(start.replace('Z', '+00:00'))
                    busy_slots.append(f"{start_time.hour:02d}:{start_time.minute:02d}")

            available_slots = [slot for slot in all_slots if slot not in busy_slots]

            return AvailableSlotsResponse(
                date=date_str,
                available_slots=available_slots,
                duration=duration
            )

        except Exception as e:
            logger.error(f"Error getting available slots: {e}")
            return await self._get_mock_slots(date_str, duration)

    async def _get_mock_slots(self, date_str: str, duration: int) -> AvailableSlotsResponse:
        """Retorna slots mockados para desenvolvimento"""
        slots = []
        for hour in range(9, 18):
            slots.append(f"{hour:02d}:00")
            slots.append(f"{hour:02d}:30")
        
        return AvailableSlotsResponse(
            date=date_str,
            available_slots=slots,
            duration=duration
        )

    async def create_appointment(self, appointment: AppointmentCreate) -> dict:
        """Cria um agendamento no Google Calendar"""
        if not self.service:
            return {
                "message": "Appointment created (mock mode - Google Calendar not configured)",
                "appointment": {
                    "id": "mock-appointment-123",
                    "date": appointment.date,
                    "time": appointment.time
                }
            }

        try:
            # Converter data e hora
            date_time_str = f"{appointment.date}T{appointment.time}:00"
            start_datetime = datetime.fromisoformat(date_time_str)
            end_datetime = start_datetime + timedelta(hours=1)

            event = {
                'summary': f'{appointment.service} - {appointment.name}',
                'description': f'''
Cliente: {appointment.name}
Email: {appointment.email}
Telefone: {appointment.phone}
Serviço: {appointment.service}
{f"Mensagem: {appointment.message}" if appointment.message else ""}
                '''.strip(),
                'start': {
                    'dateTime': start_datetime.isoformat(),
                    'timeZone': 'America/Sao_Paulo',
                },
                'end': {
                    'dateTime': end_datetime.isoformat(),
                    'timeZone': 'America/Sao_Paulo',
                },
                'attendees': [
                    {'email': appointment.email}
                ],
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'email', 'minutes': 24 * 60},
                        {'method': 'popup', 'minutes': 60},
                    ],
                },
            }

            created_event = self.service.events().insert(
                calendarId=self.calendar_id,
                body=event,
                sendUpdates='all'
            ).execute()

            logger.info(f"Appointment created: {created_event['id']}")

            return {
                "message": "Appointment created successfully",
                "appointment": {
                    "id": created_event['id'],
                    "htmlLink": created_event.get('htmlLink'),
                    "startTime": start_datetime.isoformat(),
                    "endTime": end_datetime.isoformat()
                }
            }

        except Exception as e:
            logger.error(f"Error creating appointment: {e}")
            raise

    async def get_appointments(self, start_date: str = None, end_date: str = None) -> dict:
        """Lista agendamentos"""
        if not self.service:
            return {"appointments": [], "count": 0}

        try:
            time_min = (datetime.fromisoformat(start_date) if start_date 
                       else datetime.now()).isoformat() + 'Z'
            time_max = (datetime.fromisoformat(end_date) if end_date 
                       else datetime.now() + timedelta(days=30)).isoformat() + 'Z'

            events_result = self.service.events().list(
                calendarId=self.calendar_id,
                timeMin=time_min,
                timeMax=time_max,
                singleEvents=True,
                orderBy='startTime'
            ).execute()

            events = events_result.get('items', [])

            return {
                "appointments": events,
                "count": len(events)
            }

        except Exception as e:
            logger.error(f"Error getting appointments: {e}")
            return {"appointments": [], "count": 0}

    async def cancel_appointment(self, event_id: str):
        """Cancela um agendamento"""
        if not self.service:
            return

        try:
            self.service.events().delete(
                calendarId=self.calendar_id,
                eventId=event_id,
                sendUpdates='all'
            ).execute()

            logger.info(f"Appointment cancelled: {event_id}")

        except Exception as e:
            logger.error(f"Error cancelling appointment: {e}")
            raise
