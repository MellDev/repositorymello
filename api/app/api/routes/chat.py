from fastapi import APIRouter, Request, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse, ChatMessage
from app.services.chat_service import chat_service
from app.config import settings
import hashlib
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

# In-memory session tracking (consider using Redis for production)
session_limits: dict[str, int] = {}

def get_client_identifier(request: Request) -> str:
    """Create unique identifier from IP and User-Agent"""
    client_ip = request.client.host
    user_agent = request.headers.get("user-agent", "")
    identifier = f"{client_ip}:{user_agent}"
    return hashlib.sha256(identifier.encode()).hexdigest()

@router.post("/chat", response_model=ChatResponse)
async def chat(request_data: ChatRequest, request: Request):
    try:
        # Get or create session ID
        session_id = request_data.session_id or get_client_identifier(request)
        
        # Check rate limit
        current_count = session_limits.get(session_id, 0)
        max_messages = settings.max_chat_messages_per_session
        
        if current_count >= max_messages:
            return ChatResponse(
                response="Você atingiu o limite de mensagens. Recarregue a página para continuar.",
                session_id=session_id,
                messages_remaining=0,
                limit_reached=True
            )
        
        # Increment message count
        session_limits[session_id] = current_count + 1
        
        # Prepare messages for OpenAI
        messages = [
            {"role": msg.role, "content": msg.content}
            for msg in request_data.conversation_history
        ]
        messages.append({"role": "user", "content": request_data.message})
        
        # Get response from OpenAI
        response_text = await chat_service.get_chat_response(messages)
        
        # Calculate remaining messages
        messages_remaining = max_messages - session_limits[session_id]
        
        return ChatResponse(
            response=response_text,
            session_id=session_id,
            messages_remaining=messages_remaining,
            limit_reached=messages_remaining == 0
        )
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/chat/status/{session_id}")
async def get_chat_status(session_id: str):
    current_count = session_limits.get(session_id, 0)
    max_messages = settings.max_chat_messages_per_session
    return {
        "messages_used": current_count,
        "messages_remaining": max_messages - current_count,
        "limit_reached": current_count >= max_messages
    }

@router.delete("/chat/session/{session_id}")
async def reset_chat_session(session_id: str):
    if session_id in session_limits:
        del session_limits[session_id]
    return {"message": "Session reset successfully"}
