import snowflake.connector
from snowflake.connector import SnowflakeConnection

from app.config import Config
from app.logger import logger


def get_connection() -> SnowflakeConnection:
    """
    Creates and returns a Snowflake connection.

    Returns:
        SnowflakeConnection: Active Snowflake connection

    Raises:
        Exception: If connection fails.
    """

    try:
        logger.info("Connecting to Snowflake...")

        conn = snowflake.connector.connect(
            account=Config.ACCOUNT,
            user=Config.USER,
            password=Config.PASSWORD,
            warehouse=Config.WAREHOUSE,
            database=Config.DATABASE,
            schema=Config.SCHEMA,
            role=Config.ROLE,
        )

        logger.info("Connected to Snowflake successfully.")

        return conn

    except Exception as e:
        logger.exception("Failed to connect to Snowflake.")
        raise Exception(f"Snowflake Connection Error: {e}")