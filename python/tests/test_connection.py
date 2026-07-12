from app.connection import get_connection
from app.logger import logger


def main():

    conn = None

    try:
        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                CURRENT_ACCOUNT(),
                CURRENT_DATABASE(),
                CURRENT_SCHEMA(),
                CURRENT_WAREHOUSE(),
                CURRENT_VERSION();
        """)

        result = cursor.fetchone()

        print("\n========== Snowflake Connection ==========\n")

        print(f"Account      : {result[0]}")
        print(f"Database     : {result[1]}")
        print(f"Schema       : {result[2]}")
        print(f"Warehouse    : {result[3]}")
        print(f"Version      : {result[4]}")

        print("\nConnection Successful!")

    except Exception as e:

        logger.exception("Connection Test Failed")

        print(e)

    finally:

        if conn:

            conn.close()

            logger.info("Snowflake connection closed.")


if __name__ == "__main__":
    main()