from app.connection import get_connection


def test_connection():

    conn = get_connection()

    assert conn is not None

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

    assert result is not None

    conn.close()