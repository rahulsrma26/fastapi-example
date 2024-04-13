from typing import List, Dict
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    price: float
    quantity: int


class Message(BaseModel):
    message: str


db: Dict[int, Item] = {
    1: Item(id=1, name="Laptop", price=999.99, quantity=5),
    2: Item(id=2, name="Headphones", price=149.99, quantity=10),
    3: Item(id=3, name="Smartphone", price=799.99, quantity=8),
    4: Item(id=4, name="Tablet", price=399.99, quantity=12),
    5: Item(id=5, name="Smartwatch", price=249.99, quantity=6),
}

shopping_cart: Dict[int, Item] = {}


@app.get("/")
def read_root():
    return {"Hello": "World"}


# GET method to retrieve all items in recommended page
@app.get("/items/", response_model=List[Item])
async def all_items():
    return db.values()


# GET method to retrieve all items in the shopping cart
@app.get("/cart/", response_model=List[Item])
async def get_cart():
    return shopping_cart.values()


# POST method to add an item to the shopping cart
@app.post("/cart/", response_model=Item, responses={404: {"model": Message}})
async def add_to_cart(item: Item):
    if not item.id in db:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    cart_item = item.model_copy()
    if item.quantity < cart_item.quantity:
        JSONResponse(status_code=404, content={"message": "Out of stock"})
    shopping_cart[cart_item.id] = cart_item
    return cart_item


# PUT method to update an item in the shopping cart
@app.put("/cart/{item_id}/", response_model=Item, responses={404: {"model": Message}})
async def update_cart_item(item: Item):
    if not item.id in db:
        return JSONResponse(status_code=404, content={"message": "Item doesn't exist"})
    if not item.id in shopping_cart:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    return await add_to_cart(item=item)


# DELETE method to remove an item from the shopping cart
@app.delete("/cart/{item_id}/")
async def delete_cart_item(item_id: int, responses={404: {"model": Message}}):
    if item_id not in shopping_cart:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    del shopping_cart[item_id]
    return {"message": "Item deleted successfully"}
