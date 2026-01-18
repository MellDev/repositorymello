from fastapi import APIRouter, HTTPException
from typing import Optional
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


# Projetos mockados (em produção viria do banco)
PROJECTS = [
    {
        "id": "konoha-barber",
        "name": "Konoha Barber",
        "slug": "konoha-barber",
        "description": "Sistema completo de agendamento para barbearia",
        "long_description": "Plataforma web completa com Google Calendar, IA e WhatsApp",
        "technologies": ["React", "Node.js", "Google Calendar", "OpenAI"],
        "features": [
            "Integração Google Calendar API",
            "IA para gestão automatizada",
            "Notificações WhatsApp",
            "Dashboard administrativo"
        ],
        "status": "completed",
        "category": "web",
        "github_url": "https://github.com/MellDev/konoha-barber",
        "demo_url": "https://konoha-barber.vercel.app"
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
