from typing import Optional

from pydantic import BaseModel, ConfigDict

class BookBase(BaseModel):
    title: str
    author : str
    year: int

class BookCreate(BookBase):
    """Schema for creating a new book"""
    pass

class BookUpdate(BaseModel):
    """Schema for updating a book"""
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None

class Book(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class BookResponse(BaseModel):
    title: str
    author: str
    year: int

    model_config = ConfigDict(from_attributes=True)
