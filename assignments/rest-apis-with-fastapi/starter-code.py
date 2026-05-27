# Starter Code: REST APIs with FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for assignment practice.
books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
    {"id": 2, "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015},
]


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


@app.get("/books")
def list_books():
    # Task 1: Return all books.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # Task 1: Return one book by ID, or raise 404.
    pass


@app.post("/books")
def create_book(payload: BookCreate):
    # Task 1: Add a new book and return it.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, payload: BookCreate):
    # Task 2: Update an existing book by ID, or raise 404.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # Task 2: Delete a book by ID, or raise 404.
    pass


# Run locally with:
# uvicorn starter-code:app --reload
