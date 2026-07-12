from app.config import Config


def test_paths_exist():

    assert Config.SQL_DIR.exists()
    assert Config.RAW_DATA_DIR.exists()