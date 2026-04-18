from fastapi import FastAPI, HTTPException
import psycopg
from psycopg.rows import dict_row
from typing import Optional

DB_PATH = "dbname=postgres user=postgres password=postgres host=localhost port=5432"
app = FastAPI()

def get_db():
    return psycopg.connect(DB_PATH)

@app.get("/inventory/get")
def get_inventory(
    category: Optional[str] = None,
    stock_le: Optional[int] = None,
    stock_ge: Optional[int] = None,
):
    query = "SELECT * FROM inventory WHERE 1=1"
    params = []

    if category is not None:
        query += " AND category = %s"
        params.append(category)

    if stock_le is not None:
        query += " AND stock_qty <= %s"
        params.append(stock_le)

    if stock_ge is not None:
        query += " AND stock_qty >= %s"
        params.append(stock_ge)

    try:
        conn = get_db()
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(query, params)
            rows = cur.fetchall()

    except Exception as ex:
        print(f"エラー発生: {ex}")
        raise HTTPException(status_code=500, detail=str(ex))

    finally:
        conn.close()

    return rows
