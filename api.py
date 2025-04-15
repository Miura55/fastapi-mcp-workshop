from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="MCP API",
    description="API for managing the MCP system",
    version="0.1.0",
)

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
    return [
        Item(id=1, name="Item 1", description="Description for item 1", price=10.0, tags=["tag1", "tag2"]),
        Item(id=2, name="Item 2", description="Description for item 2", price=20.0, tags=["tag3"]),
    ]
