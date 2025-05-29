from fastapi import FastAPI

app  = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/{name}")
def hello_name(name):
    return {"message": f"Hello {name}"}

@app.post("/")
def create_item(item: str):
    return {"message": f"Item created: {item}"}