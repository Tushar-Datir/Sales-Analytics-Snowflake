from pathlib import Path
from snowflake.connector import SnowflakeConnection

from app.logger import logger


class SQLExecutor:
    """
    Executes SQL scripts against Snowflake.
    """

    def __init__(self, connection: SnowflakeConnection):
        self.connection = connection

    def execute_file(self, sql_file: Path):

        if not sql_file.exists():
            raise FileNotFoundError(f"{sql_file} not found.")

        logger.info(f"Executing SQL File : {sql_file.name}")

        cursor = self.connection.cursor()

        try:

            sql = sql_file.read_text(encoding="utf-8")

            statements = [
                stmt.strip()
                for stmt in sql.split(";")
                if stmt.strip()
            ]

            logger.info(f"Total SQL Statements : {len(statements)}")

            for index, statement in enumerate(statements, start=1):

                logger.info(f"Executing Statement {index}")

                cursor.execute(statement)

            self.connection.commit()

            logger.info(f"{sql_file.name} executed successfully.")

        except Exception as e:

            self.connection.rollback()

            logger.exception(f"Error executing {sql_file.name}")

            raise

        finally:

            cursor.close()