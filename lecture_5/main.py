from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from database import get_db, engine
from models import model
from schemas import schema
from repositories.repository import BookRepo
from sqlalchemy.orm import Session
import uvicorn
from typing import List, Optional

app = FastAPI(
    title="Book API Application",
    description="Book API Application (Innowise Lecture #5)",
    version="1.0.0",
)

model.Base.metadata.create_all(bind=engine)

@app.exception_handler(Exception)
def validation_exception_handler(request: Request, err: Exception):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(
        status_code=400,
        content={"message": f"{base_error_message}. Detail: {err}"}
    )

@app.post('/books', tags=["Book"], response_model=schema.Book, status_code=201)
def create_book(book_request: schema.BookCreate, db: Session = Depends(get_db)):
    """ Create a new book and store it in the database """
    repo = BookRepo(db)
    db_book = repo.fetch_by_title(title=book_request.title)
    if db_book:
        raise HTTPException(
            status_code=400,
            detail="Book already exists!"
        )
    return repo.create_book(book=book_request)

@app.get("/books", tags=["Book"], response_model=List[schema.Book])
def get_all_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """ Get all books stored in the database with pagination. """
    repo = BookRepo(db)
    return repo.fetch_all(skip=skip, limit=limit)

@app.delete('/books/{book_id}', tags=["Book"])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """ Delete a book by its ID """
    repo = BookRepo(db)
    db_book = repo.fetch_by_id(book_id=book_id)
    if db_book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found with the given ID"
        )
    repo.delete_book(book_id=book_id)
    return {"message": "Book deleted successfully!"}

@app.post("/books/{book_id}/edit", tags=["Book"], response_model=schema.BookResponse)
def edit_book(book_id: int, book_request: schema.BookUpdate, db: Session = Depends(get_db)):
    """ Update a Book by its ID """
    repo = BookRepo(db)
    db_book = repo.fetch_by_id(book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    update_data = book_request.model_dump(exclude_unset=True, exclude_none=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)

    return repo.update_book(book_data=db_book)

@app.get('/books/search', tags=["Book"], response_model=List[schema.Book])
def search_books(title: Optional[str] = None,
                 author: Optional[str] = None,
                 year: Optional[int] = None,
                 db: Session = Depends(get_db)
                 ):
    """ Search books by title, author, or year """
    repo = BookRepo(db)
    results = repo.search_book(title=title, author=author, year=year)
    if not results:
        raise HTTPException(
            status_code=404,
            detail="No books found")
    return results

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)