from typing import Union
import sqlalchemy
from db import get_db, close_db

from fastapi import FastAPI

app = FastAPI()
print("Hello, World!")

@app.get("/")
def read_root():
    return "Hello, World!"


@app.get("/health")
async def health():
    db = await get_db()
    health = "BAD"
    try:
        result = await db.execute("SELECT NOW()")
        result = result.one()
        health = "OK"
        print(f"/health reported OK including database connection: {result}")
    except sqlalchemy.exc.OperationalError as e:
        msg = f"sqlalchemy.exc.OperationalError: {e}"
        print(msg)
    except Exception as e:
        msg = f"Error performing healthcheck: {e}"
        print(msg)
    return health


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}