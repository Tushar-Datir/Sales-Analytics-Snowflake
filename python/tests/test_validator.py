from app.config import Config
from app.validator import DataValidator


def main():

    csv_file = Config.RAW_DATA_DIR / "train.csv"

    validator = DataValidator(csv_file)

    validator.load()

    validator.summary()


if __name__ == "__main__":
    main()