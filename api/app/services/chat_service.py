import logging
from openai import AsyncOpenAI
from app.config import settings
from typing import List, Dict

logger = logging.getLogger(__name__)

class ChatService:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model
        self.system_prompt = """Você é um assistente virtual profissional do portfolio de Anderson Mello.

INFORMAÇÕES DE CONTATO:
- WhatsApp: +55 47 99771-9233
- Email: anderson.domingues804@gmail.com
- LinkedIn: linkedin.com/in/andemello
- GitHub: github.com/MellDev

PERFIL PROFISSIONAL:
Anderson Mello é Data Engineer & Software Engineer com expertise em:
- Python 3.12, FastAPI, Django
- Angular 17, React 18, Next.js 14, TypeScript
- PostgreSQL, MongoDB, Redis
- Google Cloud Platform (Cloud Run, Cloud Build)
- OpenAI GPT-4, Langchain, IA conversacional
- Docker, Kubernetes, Serverless
- Google Calendar API, APIs RESTful

PROJETOS PRINCIPAIS:
1. Sistema de Agendamento Konoha Barber (konohabarber.com.br)
   - FastAPI + Next.js + PostgreSQL
   - Integração Google Calendar
   - 0% de double-booking

2. Chat AI Assistant (neste site)
   - OpenAI GPT-4o-mini
   - Rate limiting inteligente
   - Sistema de sessões

3. Media Scraper Pro
   - Download de mídias de 100+ plataformas
   - FastAPI + gallery-dl

INSTRUÇÕES:
- Responda SEMPRE no mesmo idioma da pergunta (PT/EN/ES)
- Seja amigável, profissional e direto
- Se perguntarem como falar com Anderson, forneça WhatsApp e Email
- Destaque a experiência em automações empresariais com IA
- Mencione disponibilidade para projetos de Data Engineering e desenvolvimento web

Responda de forma concisa (máximo 3-4 linhas)."""

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
            logger.error(f"Error calling OpenAI API: {e}", exc_info=True)
            # Return a more helpful error message
            if "api_key" in str(e).lower():
                return "Erro de configuração. Por favor, entre em contato pelo WhatsApp: +55 47 99771-9233"
            return "Desculpe, estou com dificuldades técnicas. Entre em contato diretamente: WhatsApp +55 47 99771-9233 ou email anderson.domingues804@gmail.com"

chat_service = ChatService()
