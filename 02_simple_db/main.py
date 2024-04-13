from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

db: List[Item] = [
    Item(id=1, name="Laptop", price=999.99, quantity=5),
    Item(id=2, name="Headphones", price=149.99, quantity=10),
    Item(id=3, name="Smartphone", price=799.99, quantity=8),
    Item(id=4, name="Tablet", price=399.99, quantity=12),
    Item(id=5, name="Smartwatch", price=249.99, quantity=6)
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

# GET method to retrieve all items in recommended page
@app.get("/items/", response_model=List[Item])
async def all_items():
    return db
