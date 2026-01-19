from fastapi import APIRouter, HTTPException
from typing import Optional
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


# Projetos mockados (em produção viria do banco)
PROJECTS = [
    {
        "id": "konoha-barber",
        "name": "Sistema de Agendamento Inteligente",
        "slug": "konoha-barber",
        "description": "Sistema completo de agendamento para barbearias com verificação híbrida, sincronização Google Calendar e gestão multi-barbeiros",
        "long_description": """Sistema de agendamento inteligente com arquitetura serverless, 
        verificação híbrida (Google Calendar + Banco Local), precificação dinâmica e interface intuitiva. 
        Previne 100% de double-booking através de dupla verificação e sincronização bidirecional.""",
        "technologies": [
            "Python 3.12",
            "FastAPI 0.104+",
            "PostgreSQL 15+",
            "Next.js 14",
            "React 18",
            "TypeScript 5.x",
            "Google Calendar API v3",
            "Tailwind CSS",
            "JWT Auth",
            "Neon Database"
        ],
        "features": [
            "Verificação Híbrida de Disponibilidade (Google Calendar + Banco Local)",
            "Grid Visual de Horários com Estados (Disponível/Ocupado/Selecionado)",
            "Multi-Calendário (Suporte a Múltiplos Barbeiros)",
            "Sincronização Bidirecional com Google Calendar",
            "Precificação Dinâmica (Descontos por Horário e Dia)",
            "Prevenção Total de Double-Booking",
            "Autenticação JWT com Scopes (Cliente/Barbeiro/Admin)",
            "TimeSlotPicker Component Customizado",
            "API REST com Documentação Automática (OpenAPI/Swagger)",
            "Type Safety Total (TypeScript + Pydantic)",
            "Deploy Serverless em Cloud Run",
            "Database com TIMESTAMPTZ Nativo",
            "Interface Mobile-First Responsiva"
        ],
        "highlights": [
            "🏆 0% de Double-Booking através de verificação híbrida",
            "🎯 UX Superior com grid visual de disponibilidade",
            "⚡ Serverless Autoscaling (0-100 instâncias)",
            "🔄 Sincronização Real-Time com Google Calendar",
            "💰 Precificação Inteligente com Regras Automáticas",
            "🔒 Type Safety Total em Todo o Stack",
            "📱 Design Mobile-First com Tailwind CSS",
            "🌐 Multi-Tenant Ready para Múltiplos Barbeiros"
        ],
        "architecture": {
            "backend": "FastAPI + Python 3.12 + PostgreSQL (Neon)",
            "frontend": "Next.js 14 + React 18 + TypeScript",
            "auth": "JWT com OAuth2PasswordBearer",
            "integration": "Google Calendar API v3 com Service Account",
            "hosting": "Cloud Run (Backend + Frontend)",
            "database": "PostgreSQL Serverless (Neon) com TIMESTAMPTZ"
        },
        "differentials": [
            "Verificação híbrida previne 100% de conflitos de horário",
            "Calendários individuais por barbeiro para escalabilidade",
            "Precificação dinâmica otimiza ocupação e receita",
            "Interface intuitiva reduz erros de agendamento",
            "Type safety detecta bugs em desenvolvimento",
            "Sincronização bidirecional mantém consistência total"
        ],
        "status": "completed",
        "category": "web",
        "github_url": "https://github.com/MellDev/KonohaBarber",
        "demo_url": "https://konoha-barber.vercel.app",
        "api_docs": "https://konoha-barber-api.run.app/docs"
    },
    {
        "id": "media-scraper",
        "name": "Media Scraper Pro",
        "slug": "media-scraper",
        "description": "Ferramenta avançada de scraping com gallery-dl",
        "long_description": "Sistema profissional de scraping para 100+ plataformas",
        "technologies": ["Python", "FastAPI", "gallery-dl", "React"],
        "features": [
            "Suporte 100+ plataformas",
            "Download em lote",
            "API REST completa",
            "Sistema de filas"
        ],
        "status": "completed",
        "category": "automation",
        "github_url": "https://github.com/MellDev/media-scraper"
    },
    {
        "id": "ai-automation",
        "name": "AI Automation Suite",
        "slug": "ai-automation",
        "description": "Suite de automações com IA",
        "long_description": "Ferramentas de automação com inteligência artificial",
        "technologies": ["Python", "Langchain", "OpenAI", "Selenium"],
        "features": [
            "Processamento de linguagem natural",
            "Chatbots inteligentes",
            "Automação de tarefas",
            "Web scraping avançado"
        ],
        "status": "in-progress",
        "category": "ai",
        "github_url": "https://github.com/MellDev/ai-automation"
    }
]


@router.get("/")
async def get_projects(
    category: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[int] = None
):
    """
    Lista todos os projetos
    """
    projects = PROJECTS.copy()
    
    if category:
        projects = [p for p in projects if p["category"] == category]
    
    if status:
        projects = [p for p in projects if p["status"] == status]
    
    if limit:
        projects = projects[:limit]
    
    return {
        "projects": projects,
        "count": len(projects),
        "total": len(PROJECTS)
    }


@router.get("/{project_id}")
async def get_project_by_id(project_id: str):
    """
    Retorna detalhes de um projeto específico
    """
    project = next((p for p in PROJECTS if p["id"] == project_id or p["slug"] == project_id), None)
    
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return {"project": project}
