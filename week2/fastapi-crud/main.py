from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD API"}

# Get all items
@app.get("/items")
def get_items():
    pass

# Create a new item
@app.post("/items")
def create_item(item: str):
    pass

# Update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: str):
    pass

# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    pass