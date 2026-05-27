# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice creating endpoints, handling request data, and returning JSON responses. You will learn how backend services organize routes and validate input data.

## 📝 Tasks

### 🛠️ Build Core API Endpoints

#### Description
Create a FastAPI app with endpoints for managing a small in-memory list of books. Implement routes to list all books, get one book by ID, and create a new book.

#### Requirements
Completed program should:

- Create a FastAPI application in `starter-code.py`.
- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return a single book or a 404 error if not found.
- Implement `POST /books` to add a new book and return the created record.


### 🛠️ Add Validation and Update/Delete Routes

#### Description
Improve the API by validating incoming data and adding update and delete functionality for existing books.

#### Requirements
Completed program should:

- Use a Pydantic model to validate the book payload (`title`, `author`, `year`).
- Implement `PUT /books/{book_id}` to update a book by ID.
- Implement `DELETE /books/{book_id}` to remove a book by ID.
- Return clear status codes and JSON messages for success and error cases.
