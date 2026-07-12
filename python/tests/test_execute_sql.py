from app.connection import get_connection
from app.execute_sql import SQLExecutor
from app.config import Config


def main():

    conn = get_connection()

    try:
        executor = SQLExecutor(conn)

        sql_file = Config.SQL_DIR / "09_analytics.sql"

        executor.execute_file(sql_file)

        print("SQL Executed Successfully!")

    finally:
        conn.close()


if __name__ == "__main__":
    main()