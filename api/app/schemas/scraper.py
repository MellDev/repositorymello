from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from enum import Enum


class QualityEnum(str, Enum):
    best = "best"
    p1080 = "1080p"
    p720 = "720p"
    p480 = "480p"


class DownloadRequest(BaseModel):
    url: HttpUrl
    quality: QualityEnum = QualityEnum.best
    include_metadata: bool = False


class DownloadResponse(BaseModel):
    message: str
    job_id: str
    status_url: str


class JobStatusEnum(str, Enum):
    processing = "processing"
    downloading = "downloading"
    completed = "completed"
    failed = "failed"


class JobStatus(BaseModel):
    id: str
    url: str
    status: JobStatusEnum
    progress: int
    started_at: str
    completed_at: Optional[str] = None
    files: Optional[List[dict]] = None
    error: Optional[str] = None
