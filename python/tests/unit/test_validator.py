from app.config import Config
from app.validator import DataValidator


def test_validator():

    csv_file = Config.RAW_DATA_DIR / "train.csv"

    validator = DataValidator(csv_file)

    df = validator.load()

    validator.summary()

    assert df is not None
    assert len(df) > 0
    assert "SALES" in df.columns