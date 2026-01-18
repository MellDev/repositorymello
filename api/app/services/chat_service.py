import logging
from openai import AsyncOpenAI
from app.config import settings
from typing import List, Dict

logger = logging.getLogger(__name__)

class ChatService:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model
        self.system_prompt = """Você é um assistente virtual do portfolio de Anderson Mello, 
        um Data Engineer e Software Engineer. Você deve responder perguntas sobre suas habilidades, 
        projetos e experiência de forma amigável e profissional. 
        
        Responda sempre no mesmo idioma da pergunta (português, inglês ou espanhol).
        
        Informações sobre Anderson:
        - Data Engineer e Software Engineer
        - Especialista em Python, FastAPI, Angular, Cloud Computing
        - Contato: LinkedIn (andemello), WhatsApp (+55 47 99771-9233)
        - Email: anderson.domingues804@gmail.com
        
        Mantenha respostas concisas e diretas."""

    async def get_chat_response(self, messages: List[Dict[str, str]]) -> str:
        try:
            # Add system prompt at the beginning
            full_messages = [{"role": "system", "content": self.system_prompt}] + messages
            
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=full_messages,
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling OpenAI API: {e}")
            return "Desculpe, ocorreu um erro ao processar sua mensagem. Por favor, tente novamente."

chat_service = ChatService()
