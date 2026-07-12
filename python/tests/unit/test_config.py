from app.config import Config


def test_config():

    assert Config.ACCOUNT is not None
    assert Config.ACCOUNT != ""

    assert Config.WAREHOUSE is not None
    assert Config.WAREHOUSE != ""

    assert Config.DATABASE is not None
    assert Config.DATABASE != ""

    assert Config.SQL_DIR.exists()

    assert Config.RAW_DATA_DIR.exists()

    print("\nConfiguration Loaded Successfully")