from fastapi import APIRouter, HTTPException
import logging

from app.schemas.contact import ContactMessage
from app.services.email_service import EmailService

logger = logging.getLogger(__name__)
router = APIRouter()
email_service = EmailService()


@router.post("/")
async def send_contact_message(message: ContactMessage):
    """
    Envia mensagem de contato por email
    """
    try:
        await email_service.send_contact_email(message)
        return {
            "message": "Message sent successfully",
            "success": True
        }
    except Exception as e:
        logger.error(f"Error sending contact message: {e}")
        raise HTTPException(status_code=500, detail="Failed to send message")
