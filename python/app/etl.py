from app.config import Config
from app.connection import get_connection
from app.execute_sql import SQLExecutor
from app.logger import logger
from app.uploader import SnowflakeUploader


def main():

    logger.info("=" * 80)
    logger.info("SALES ANALYTICS ETL PIPELINE STARTED")
    logger.info("=" * 80)

    conn = None

    try:

        # ======================================================
        # STEP 1 : Connect to Snowflake
        # ======================================================

        conn = get_connection()
        executor = SQLExecutor(conn)

        # ======================================================
        # STEP 2 : Create Schemas & Tables FIRST
        # ======================================================

        setup_scripts = [
            "02_create_schemas.sql",
            "03_create_tables.sql"
        ]

        for script in setup_scripts:

            logger.info("-" * 80)
            logger.info(f"Executing : {script}")

            sql_file = Config.SQL_DIR / script
            executor.execute_file(sql_file)

        # ======================================================
        # STEP 3 : Upload CSV to RAW
        # ======================================================

        logger.info("Uploading CSV to RAW.SALES_RAW")

        uploader = SnowflakeUploader(
            Config.RAW_DATA_DIR / "train.csv"
        )

        uploader.load_dataframe()
        uploader.upload()

        logger.info("RAW Upload Completed")

        # ======================================================
        # STEP 4 : Execute Remaining SQL
        # ======================================================

        remaining_scripts = [
            "04_staging.sql",
            "05_dimensions.sql",
            "06_fact.sql",
            "07_views.sql",
            "08_quality_checks.sql",
            "09_analytics.sql"
        ]

        for script in remaining_scripts:

            logger.info("-" * 80)
            logger.info(f"Executing : {script}")

            sql_file = Config.SQL_DIR / script
            executor.execute_file(sql_file)

        logger.info("=" * 80)
        logger.info("ETL PIPELINE COMPLETED SUCCESSFULLY")
        logger.info("=" * 80)

        print("\n")
        print("=" * 80)
        print("ETL PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 80)

    except Exception:

        logger.exception("ETL Pipeline Failed")
        raise

    finally:

        if conn:
            conn.close()
            logger.info("Snowflake connection closed.")


if __name__ == "__main__":
    main()