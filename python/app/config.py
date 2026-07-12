from pathlib import Path
from dotenv import load_dotenv
import os

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load Environment Variables
load_dotenv(BASE_DIR / "python" / ".env")


class Config:
    """
    Centralized configuration for the ETL project.
    """

    # Snowflake Credentials
    ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
    USER = os.getenv("SNOWFLAKE_USER")
    PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")

    # Snowflake Objects
    WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
    DATABASE = os.getenv("SNOWFLAKE_DATABASE")
    SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")
    ROLE = os.getenv("SNOWFLAKE_ROLE")

    # Project Paths
    DATA_DIR = BASE_DIR / "data"
    RAW_DATA_DIR = DATA_DIR / "raw"
    CLEAN_DATA_DIR = DATA_DIR / "cleaned"

    SQL_DIR = BASE_DIR / "sql"

    LOG_DIR = BASE_DIR / "logs"

    DASHBOARD_DIR = BASE_DIR / "dashboard"

    DOCS_DIR = BASE_DIR / "docs"