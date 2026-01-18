from fastapi import APIRouter, HTTPException, Query
from typing import Optional
import logging

from app.services.github_service import GitHubService

logger = logging.getLogger(__name__)
router = APIRouter()
github_service = GitHubService()


@router.get("/repos")
async def get_repos(username: Optional[str] = None):
    """
    Retorna lista de repositórios do usuário
    """
    try:
        repos = await github_service.get_user_repos(username)
        return repos
    except Exception as e:
        logger.error(f"Error getting repos: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/repos/{owner}/{repo}")
async def get_repo_details(owner: str, repo: str):
    """
    Retorna detalhes de um repositório específico
    """
    try:
        details = await github_service.get_repo_details(owner, repo)
        return details
    except Exception as e:
        logger.error(f"Error getting repo details: {e}")
        raise HTTPException(status_code=404, detail="Repository not found")


@router.get("/stats")
async def get_user_stats(username: Optional[str] = None):
    """
    Retorna estatísticas do usuário GitHub
    """
    try:
        stats = await github_service.get_user_stats(username)
        return stats
    except Exception as e:
        logger.error(f"Error getting user stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/contributions")
async def get_contributions(username: Optional[str] = None):
    """
    Retorna contribuições do usuário
    """
    try:
        contributions = await github_service.get_contributions(username)
        return contributions
    except Exception as e:
        logger.error(f"Error getting contributions: {e}")
        raise HTTPException(status_code=500, detail=str(e))
