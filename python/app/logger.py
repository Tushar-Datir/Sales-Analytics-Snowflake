import logging
from pathlib import Path
from app.config import Config


def setup_logger(name: str = "SalesAnalyticsETL"):
    """
    Configure and return a logger.
    """

    # Create logs directory if it doesn't exist
    Config.LOG_DIR.mkdir(parents=True, exist_ok=True)

    log_file = Config.LOG_DIR / "etl.log"

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()