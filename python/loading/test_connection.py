"""
Phase 10:
Azure SQL Connection Test
"""

from sqlalchemy import text
from python.config.database_config import get_engine


def test_connection():

    try:
        engine = get_engine()

        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT DB_NAME() AS DatabaseName")
            )

            for row in result:
                print("Connected Successfully ✅")
                print("Database:", row[0])

    except Exception as e:
        print("Connection Failed ❌")
        print(e)


if __name__ == "__main__":
    test_connection()