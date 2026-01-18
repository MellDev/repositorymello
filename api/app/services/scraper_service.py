import asyncio
import subprocess
import os
import uuid
from datetime import datetime
from pathlib import Path
import logging
from typing import Dict, Optional

from app.config import settings
from app.schemas.scraper import DownloadRequest, DownloadResponse, JobStatus, JobStatusEnum

logger = logging.getLogger(__name__)

# Armazenamento de jobs em memória (em produção use Redis ou banco)
jobs_storage: Dict[str, JobStatus] = {}


class ScraperService:
    def __init__(self):
        self.download_path = Path(settings.download_path)
        self.download_path.mkdir(parents=True, exist_ok=True)

    async def start_download(self, request: DownloadRequest) -> DownloadResponse:
        """Inicia download de mídia"""
        job_id = f"job_{datetime.now().strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:8]}"

        # Criar job
        job = JobStatus(
            id=job_id,
            url=str(request.url),
            status=JobStatusEnum.processing,
            progress=0,
            started_at=datetime.now().isoformat()
        )
        jobs_storage[job_id] = job

        # Processar download em background
        asyncio.create_task(self._process_download(job_id, request))

        return DownloadResponse(
            message="Download started",
            job_id=job_id,
            status_url=f"/api/scraper/status/{job_id}"
        )

    async def _process_download(self, job_id: str, request: DownloadRequest):
        """Processa o download em background"""
        job = jobs_storage[job_id]

        try:
            job_dir = self.download_path / job_id
            job_dir.mkdir(exist_ok=True)

            # Atualizar status
            job.status = JobStatusEnum.downloading
            job.progress = 50

            # Comando gallery-dl
            cmd = [
                "gallery-dl",
                "--dest", str(job_dir),
            ]

            if request.include_metadata:
                cmd.append("--write-metadata")

            cmd.append(str(request.url))

            logger.info(f"Executing: {' '.join(cmd)}")

            # Executar download
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )

            stdout, stderr = await process.communicate()

            if process.returncode == 0:
                # Sucesso
                files = []
                for file_path in job_dir.glob("*"):
                    if file_path.is_file():
                        files.append({
                            "name": file_path.name,
                            "size": file_path.stat().st_size
                        })

                job.status = JobStatusEnum.completed
                job.progress = 100
                job.completed_at = datetime.now().isoformat()
                job.files = files

                logger.info(f"Download completed for job {job_id}")
            else:
                # Erro
                error_msg = stderr.decode() if stderr else "Unknown error"
                job.status = JobStatusEnum.failed
                job.error = error_msg
                logger.error(f"Download failed for job {job_id}: {error_msg}")

        except FileNotFoundError:
            job.status = JobStatusEnum.failed
            job.error = "gallery-dl not found. Please install it: pip install gallery-dl"
            logger.error(f"gallery-dl not found for job {job_id}")
        except Exception as e:
            job.status = JobStatusEnum.failed
            job.error = str(e)
            logger.error(f"Download error for job {job_id}: {e}")

    async def get_job_status(self, job_id: str) -> Optional[JobStatus]:
        """Retorna status do job"""
        return jobs_storage.get(job_id)

    async def get_supported_platforms(self) -> dict:
        """Lista plataformas suportadas"""
        platforms = [
            {"name": "Instagram", "domain": "instagram.com", "icon": "instagram"},
            {"name": "Twitter/X", "domain": "twitter.com", "icon": "twitter"},
            {"name": "Pinterest", "domain": "pinterest.com", "icon": "pinterest"},
            {"name": "DeviantArt", "domain": "deviantart.com", "icon": "deviantart"},
            {"name": "Flickr", "domain": "flickr.com", "icon": "flickr"},
            {"name": "Reddit", "domain": "reddit.com", "icon": "reddit"},
            {"name": "Tumblr", "domain": "tumblr.com", "icon": "tumblr"},
            {"name": "ArtStation", "domain": "artstation.com", "icon": "palette"},
            {"name": "Pixiv", "domain": "pixiv.net", "icon": "images"},
            {"name": "Imgur", "domain": "imgur.com", "icon": "image"}
        ]

        return {
            "platforms": platforms,
            "count": len(platforms),
            "note": "gallery-dl suporta 100+ plataformas. Esta é uma lista das mais populares."
        }
