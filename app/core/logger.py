"""
Logging configuration for the application.
"""
import logging
import sys
from typing import Optional

from app.core.config import settings


def setup_logger(
    name: Optional[str] = None,
    level: Optional[int] = None
) -> logging.Logger:
    """
    Set up and configure application logger.

    Args:
        name: Logger name (defaults to root logger)
        level: Logging level (defaults to INFO, or DEBUG if settings.debug=True)

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)

    # Set log level
    if level is None:
        level = logging.DEBUG if settings.debug else logging.INFO
    logger.setLevel(level)

    # Avoid duplicate handlers
    if logger.handlers:
        return logger

    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)

    # Create formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(console_handler)

    return logger


# Default application logger
logger = setup_logger("daily_briefings")
