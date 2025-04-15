from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from tinydb import TinyDB

app = FastAPI(
    title="MCP API",
    description="API for managing the MCP system",
    version="0.1.0",
)
db = TinyDB("db.json")

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tags: List[str] = []


@app.get("/items", response_model=List[Item], tags=["items"], operation_id="list_items")
async def list_items():
    """
    Retrieve a list of items.
    """
    items = db.all()
    return [Item(**item) for item in items]


@app.post("/items", response_model=Item, tags=["items"], operation_id="create_item")
async def create_item(item: Item):
    """
    Create a new item.
    """
    db.insert(item.model_dump())
    return item
