"""
Health check and status API routes.
"""
from fastapi import APIRouter
from typing import Dict, Any
from datetime import datetime

from app.core.config import settings
from app.core.logger import logger

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/")
async def health_check() -> Dict[str, Any]:
    """
    Basic health check endpoint.

    Returns:
        Health status and basic app info
    """
    return {
        "status": "healthy",
        "app_name": settings.app_name,
        "version": settings.app_version,
        "timestamp": datetime.utcnow().isoformat()
    }


@router.get("/ready")
async def readiness_check() -> Dict[str, Any]:
    """
    Readiness check for container orchestration.

    Returns:
        Readiness status and dependencies check
    """
    # TODO: Check if all required services are ready
    # TODO: Verify LLM API connectivity
    # TODO: Check database connection if applicable

    dependencies = {
        "llm_provider": "unknown",  # TODO: Check actual provider status
        "database": "not_configured",  # TODO: Check DB if needed
        "calendar_api": "not_configured"  # TODO: Check calendar API
    }

    return {
        "status": "ready",
        "dependencies": dependencies,
        "timestamp": datetime.utcnow().isoformat()
    }


@router.get("/live")
async def liveness_check() -> Dict[str, str]:
    """
    Liveness check for container orchestration.

    Returns:
        Liveness status
    """
    return {
        "status": "alive",
        "timestamp": datetime.utcnow().isoformat()
    }
