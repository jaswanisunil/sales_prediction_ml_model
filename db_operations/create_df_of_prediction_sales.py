import sqlite3
import pandas as pd

def load_data(db_path, limit=None, offset=0):
    conn = sqlite3.connect(db_path)

    query = "SELECT * FROM predicting_sales"

    if limit:
        query += f" LIMIT {limit} OFFSET {offset}"

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df