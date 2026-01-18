from pydantic import BaseModel
from typing import List, Literal

class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str

class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None
    conversation_history: List[ChatMessage] = []

class ChatResponse(BaseModel):
    response: str
    session_id: str
    messages_remaining: int
    limit_reached: bool
