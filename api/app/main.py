from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager
import logging

from app.config import settings
from app.api.routes import calendar, github, scraper, projects, contact

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events"""
    logger.info("🚀 Starting Portfolio API")
    logger.info(f"📍 Environment: {settings.node_env}")
    logger.info(f"🌐 CORS Origins: {settings.cors_origins}")
    yield
    logger.info("👋 Shutting down Portfolio API")


app = FastAPI(
    title="Portfolio API",
    description="API para portfólio com Google Calendar, GitHub, scraping e mais",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GZip Middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)


# Health Check
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "OK",
        "environment": settings.node_env,
        "version": "1.0.0"
    }


# Include routers
app.include_router(calendar.router, prefix="/api/calendar", tags=["Calendar"])
app.include_router(github.router, prefix="/api/github", tags=["GitHub"])
app.include_router(scraper.router, prefix="/api/scraper", tags=["Scraper"])
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(contact.router, prefix="/api/contact", tags=["Contact"])


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "message": "Portfolio API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
async def health():
    """Health check endpoint for Cloud Run"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.node_env == "development"
    )
