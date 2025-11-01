"""
FastAPI application entrypoint for Daily Briefings.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.logger import logger
from app.api.routes_dashboard import router as dashboard_router
from app.api.routes_health import router as health_router


# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered daily briefings with personalized planning, motivation, and wellness insights",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware configuration
# TODO: Configure allowed origins based on your deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(health_router)
app.include_router(dashboard_router)


@app.on_event("startup")
async def startup_event():
    """
    Execute on application startup.
    """
    logger.info(f"Starting {settings.app_name} v{settings.app_version}")
    logger.info(f"Debug mode: {settings.debug}")

    # TODO: Initialize connections (database, external APIs, etc.)
    # TODO: Warm up LLM connections if needed
    # TODO: Load any required data into memory

    logger.info("Application startup complete")


@app.on_event("shutdown")
async def shutdown_event():
    """
    Execute on application shutdown.
    """
    logger.info("Shutting down application...")

    # TODO: Close database connections
    # TODO: Clean up resources
    # TODO: Save any pending data

    logger.info("Application shutdown complete")


@app.get("/")
async def root():
    """
    Root endpoint with basic API information.
    """
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "status": "running",
        "docs": "/docs",
        "health": "/health/"
    }


if __name__ == "__main__":
    import uvicorn

    # Run the application
    # TODO: Configure host, port, and other uvicorn settings from environment
    uvicorn.run(
        "app.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug,
        log_level="debug" if settings.debug else "info"
    )
