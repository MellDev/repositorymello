from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

RESUME_PATH = "app/static/Anderson_Mello_Resume.pdf"

@router.get("/download")
async def download_resume():
    """
    Download Anderson Mello's resume/CV in PDF format
    """
    try:
        if not os.path.exists(RESUME_PATH):
            logger.error(f"Resume file not found at {RESUME_PATH}")
            raise HTTPException(status_code=404, detail="Resume file not found")
        
        return FileResponse(
            path=RESUME_PATH,
            media_type="application/pdf",
            filename="Anderson_Mello_Resume.pdf",
            headers={
                "Content-Disposition": "attachment; filename=Anderson_Mello_Resume.pdf"
            }
        )
    except Exception as e:
        logger.error(f"Error downloading resume: {e}")
        raise HTTPException(status_code=500, detail="Error downloading resume")

@router.get("/view")
async def view_resume():
    """
    View Anderson Mello's resume/CV in the browser
    """
    try:
        if not os.path.exists(RESUME_PATH):
            logger.error(f"Resume file not found at {RESUME_PATH}")
            raise HTTPException(status_code=404, detail="Resume file not found")
        
        return FileResponse(
            path=RESUME_PATH,
            media_type="application/pdf",
            filename="Anderson_Mello_Resume.pdf",
            headers={
                "Content-Disposition": "inline; filename=Anderson_Mello_Resume.pdf"
            }
        )
    except Exception as e:
        logger.error(f"Error viewing resume: {e}")
        raise HTTPException(status_code=500, detail="Error viewing resume")
