from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from tinydb import TinyDB, Query

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


@app.put("/items/{item_id}", response_model=Item, tags=["items"], operation_id="update_item")
async def update_item(item_id: int, item: Item):
    """
    Update an existing item.
    """
    db.update(item.model_dump(), Query().id == item_id)
    return item


@app.delete("/items/{item_id}", tags=["items"], operation_id="delete_item")
async def delete_item(item_id: int):
    """
    Delete an item.
    """
    db.remove(Query().id == item_id)
    return {"message": "Item deleted"}
