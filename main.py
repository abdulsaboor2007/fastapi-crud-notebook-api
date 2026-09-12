from fastapi import FastAPI
from pydantic import BaseModel

# Create the FastAPI application
app = FastAPI()

# In-memory database
notebooks = []


# Data blueprint
class Notebook(BaseModel):
    text: str


# ----- GET (Read) -----
@app.get("/")
def home():
    return {"message": "Notebook API is running"}


@app.get("/notebooks")
def get_notebooks():
    return notebooks


# ----- POST (Create) -----
@app.post("/notebooks")
def add_notebook(notebook: Notebook):
    new_notebook = {
        "id": len(notebooks) + 1,
        "text": notebook.text
    }
    notebooks.append(new_notebook)
    return new_notebook


# ----- PUT (Update) -----
@app.put("/notebooks/{notebook_id}")
def update_notebook(notebook_id: int, notebook: Notebook):
    for item in notebooks:
        if item["id"] == notebook_id:
            item["text"] = notebook.text
            return item
    return {"message": "Notebook not found"}


# ----- DELETE (Delete) -----
@app.delete("/notebooks/{notebook_id}")
def delete_notebook(notebook_id: int):
    for item in notebooks:
        if item["id"] == notebook_id:
            notebooks.remove(item)
            return {"message": "Notebook deleted"}
    return {"message": "Notebook not found"}
