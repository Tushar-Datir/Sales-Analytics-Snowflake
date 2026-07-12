from snowflake.connector.pandas_tools import write_pandas

from app.connection import get_connection
from app.logger import logger
from app.validator import DataValidator


class SnowflakeUploader:
    """
    Upload validated CSV data into Snowflake RAW.SALES_RAW table.
    """

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = None

    def load_dataframe(self):
        """
        Load and validate CSV.
        """

        validator = DataValidator(self.csv_file)

        self.df = validator.load()

        validator.summary()

        return self.df

    def upload(self):

        if self.df is None:
            raise ValueError(
                "DataFrame is empty. Run load_dataframe() first."
            )

        conn = get_connection()

        cursor = conn.cursor()

        try:

            logger.info("=" * 60)
            logger.info("Uploading Data to Snowflake")
            logger.info("=" * 60)

            # ---------------------------------------------
            # Convert datetime columns to ISO strings
            # ---------------------------------------------
            if "ORDER_DATE" in self.df.columns:
                self.df["ORDER_DATE"] = self.df["ORDER_DATE"].dt.strftime("%Y-%m-%d")

            if "SHIP_DATE" in self.df.columns:
                self.df["SHIP_DATE"] = self.df["SHIP_DATE"].dt.strftime("%Y-%m-%d")

            # ---------------------------------------------
            # Clear RAW table
            # ---------------------------------------------
            logger.info("Clearing RAW.SALES_RAW table...")

            cursor.execute("""
                TRUNCATE TABLE SALES_ANALYTICS_DB.RAW.SALES_RAW
            """)

            # ---------------------------------------------
            # Upload
            # ---------------------------------------------
            logger.info("Uploading data using write_pandas()...")

            success, chunks, rows, _ = write_pandas(
                conn=conn,
                df=self.df,
                table_name="SALES_RAW",
                database="SALES_ANALYTICS_DB",
                schema="RAW"
            )

            if not success:
                raise Exception("write_pandas() failed.")

            # ---------------------------------------------
            # Commit
            # ---------------------------------------------
            conn.commit()

            # ---------------------------------------------
            # Verify Upload
            # ---------------------------------------------
            cursor.execute("""
                SELECT COUNT(*)
                FROM SALES_ANALYTICS_DB.RAW.SALES_RAW
            """)

            total_rows = cursor.fetchone()[0]

            logger.info("Upload Successful")
            logger.info(f"Rows Uploaded by write_pandas : {rows}")
            logger.info(f"Rows Present in RAW Table     : {total_rows}")
            logger.info(f"Chunks Uploaded               : {chunks}")

            print("\n")
            print("=" * 60)
            print("UPLOAD SUCCESSFUL")
            print("=" * 60)
            print(f"Rows Uploaded : {rows}")
            print(f"Rows in RAW   : {total_rows}")
            print("=" * 60)

        except Exception:

            logger.exception("Upload Failed")

            raise

        finally:

            cursor.close()
            conn.close()

            logger.info("Snowflake connection closed.")