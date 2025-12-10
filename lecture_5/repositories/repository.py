from typing import Optional, List
from sqlalchemy.orm import Session
from schemas import schema
from models import model


class BookRepo:

    def __init__(self, db: Session):
        self.db = db

    def create_book(self, book: schema.BookCreate) -> model.Book:
        db_book = model.Book(title = book.title, author = book.author, year = book.year)
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book

    def fetch_by_id(self, book_id: int) -> Optional[model.Book]:
        return self.db.query(model.Book).filter(model.Book.id == book_id).first()

    def fetch_by_title(self, title: str) -> Optional[model.Book]:
        return self.db.query(model.Book).filter(model.Book.title == title).first()

    def search_book(self, title: Optional[str] = None,
               author: Optional[str] = None,
               year: Optional[int] = None) -> List[model.Book]:
        query = self.db.query(model.Book)
        if title:
            query = query.filter(model.Book.title == title)
        if author:
            query = query.filter(model.Book.author == author)
        if year:
            query = query.filter(model.Book.year == year)
        return query.all()

    def fetch_all(self, skip: int = 0, limit: int = 10) -> List[model.Book]:
        return self.db.query(model.Book).offset(skip).limit(limit).all()

    def delete_book(self, book_id: int) -> None:
        db_book = self.db.query(model.Book).filter_by(id=book_id).first()
        if db_book:
            self.db.delete(db_book)
            self.db.commit()

    def update_book(self, book_data: model.Book) -> model.Book:
        self.db.add(book_data)
        self.db.commit()
        self.db.refresh(book_data)
        return book_data

