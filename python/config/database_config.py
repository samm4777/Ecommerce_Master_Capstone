"""
Azure SQL Database Connection Configuration
Phase 10: SQL Loading
"""

import urllib.parse
from sqlalchemy import create_engine


SERVER = "retailanalytics-sameer-484848.database.windows.net"

DATABASE = "Ecommerce_Analytics"

USERNAME = "retailadmin"

PASSWORD = "S@meer.2026!!!"


def get_engine():

    connection_string = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    params = urllib.parse.quote_plus(connection_string)

    engine = create_engine(
        "mssql+pyodbc:///?odbc_connect=" + params
    )

    return engine