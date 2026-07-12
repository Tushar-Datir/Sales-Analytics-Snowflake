from pathlib import Path
import pandas as pd

from app.logger import logger


class DataValidator:
    """
    Validates and prepares CSV data before uploading to Snowflake.
    """

    DATE_COLUMNS = [
        "ORDER_DATE",
        "SHIP_DATE"
    ]

    def __init__(self, csv_file: Path):
        self.csv_file = csv_file
        self.df = None

    def load(self):
        """
        Load CSV into a Pandas DataFrame and prepare it for Snowflake.
        """

        logger.info("=" * 60)
        logger.info("Loading CSV File")
        logger.info("=" * 60)

        logger.info(f"CSV Path : {self.csv_file}")

        if not self.csv_file.exists():
            raise FileNotFoundError(f"CSV file not found: {self.csv_file}")

        try:

            # Load CSV
            self.df = pd.read_csv(self.csv_file)

            if self.df.empty:
                raise ValueError("CSV file is empty.")

            # --------------------------------------------------
            # Standardize Column Names
            # --------------------------------------------------
            self.df.columns = (
                self.df.columns
                .str.strip()
                .str.upper()
                .str.replace(" ", "_", regex=False)
                .str.replace("-", "_", regex=False)
            )

            # --------------------------------------------------
            # Convert Date Columns
            # --------------------------------------------------
            for column in self.DATE_COLUMNS:

                if column in self.df.columns:

                    self.df[column] = pd.to_datetime(
                        self.df[column],
                        format="%d/%m/%Y",
                        errors="raise"
                    )

            # --------------------------------------------------
            # Handle Postal Code
            # --------------------------------------------------
            if "POSTAL_CODE" in self.df.columns:

                self.df["POSTAL_CODE"] = (
                    self.df["POSTAL_CODE"]
                    .fillna("")
                    .astype(str)
                )

            logger.info(f"Rows Loaded    : {len(self.df)}")
            logger.info(f"Columns Loaded : {len(self.df.columns)}")
            logger.info(f"Column Names   : {list(self.df.columns)}")

            logger.info("Sample Dates:")
            logger.info(self.df[["ORDER_DATE", "SHIP_DATE"]].head())

            return self.df

        except Exception as e:
            logger.exception("Failed to load CSV.")
            raise

    def check_nulls(self):
        """
        Check NULL values in each column.
        """

        logger.info("Checking NULL values...")

        null_counts = self.df.isnull().sum()

        for column, count in null_counts.items():
            logger.info(f"{column:<20} : {count}")

        return null_counts

    def check_duplicates(self):
        """
        Check duplicate rows.
        """

        logger.info("Checking duplicate rows...")

        duplicates = self.df.duplicated().sum()

        logger.info(f"Duplicate Rows : {duplicates}")

        return duplicates

    def check_data_types(self):
        """
        Log DataFrame column data types.
        """

        logger.info("Checking data types...")

        for column, dtype in self.df.dtypes.items():
            logger.info(f"{column:<20} : {dtype}")

    def summary(self):
        """
        Print validation summary.
        """

        logger.info("=" * 60)
        logger.info("DATA VALIDATION SUMMARY")
        logger.info("=" * 60)

        logger.info(f"Total Rows    : {len(self.df)}")
        logger.info(f"Total Columns : {len(self.df.columns)}")

        self.check_data_types()
        self.check_nulls()
        self.check_duplicates()

        logger.info("=" * 60)

        return True