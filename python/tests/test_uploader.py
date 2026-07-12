from app.config import Config
from app.uploader import SnowflakeUploader


def main():

    csv_file = Config.RAW_DATA_DIR / "train.csv"

    uploader = SnowflakeUploader(csv_file)

    uploader.load_dataframe()

    uploader.upload()


if __name__ == "__main__":
    main()