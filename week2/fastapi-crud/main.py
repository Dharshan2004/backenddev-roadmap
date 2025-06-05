from fastapi import FastAPI
from database import SessionLocal
from models import TodoList, Item
import uvicorn

# Create FastAPI app 
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD API"}

# Get all items
@app.get("/items")
def get_items():
    db = SessionLocal()
    items = db.query(TodoList).all()
    return {"items": items}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    db = SessionLocal()
    item = db.query(TodoList).filter(TodoList.id == item_id).first()
    return {"item": item}

# Create a new item
@app.post("/items")
def create_item(item: Item):
    db = SessionLocal()
    new_item = TodoList(task_name=item.task_name, completed=item.completed, deadline=item.deadline)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"message": "Item created successfully", "item": new_item}

# Update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    db = SessionLocal()
    item = db.query(TodoList).filter(TodoList.id == item_id).first()
    item.task_name = item.task_name
    item.completed = item.completed
    item.deadline = item.deadline
    db.commit()
    return {"message": "Item updated successfully", "item": item}

# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db = SessionLocal()
    item = db.query(TodoList).filter(TodoList.id == item_id).first()
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)