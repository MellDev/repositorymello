from fastapi import APIRouter, HTTPException
from typing import List
import logging

from app.services.scraper_service import ScraperService
from app.schemas.scraper import DownloadRequest, DownloadResponse, JobStatus

logger = logging.getLogger(__name__)
router = APIRouter()
scraper_service = ScraperService()


@router.post("/download", response_model=DownloadResponse, status_code=202)
async def start_download(request: DownloadRequest):
    """
    Inicia download de mídia usando gallery-dl
    """
    try:
        result = await scraper_service.start_download(request)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error starting download: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status/{job_id}", response_model=JobStatus)
async def get_download_status(job_id: str):
    """
    Verifica status do download
    """
    try:
        status = await scraper_service.get_job_status(job_id)
        if not status:
            raise HTTPException(status_code=404, detail="Job not found")
        return status
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting job status: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/platforms")
async def get_supported_platforms():
    """
    Lista plataformas suportadas pelo gallery-dl
    """
    return await scraper_service.get_supported_platforms()
