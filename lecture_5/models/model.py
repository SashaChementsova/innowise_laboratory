from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(80), nullable=False, unique=True, index=True)
    author = Column(String(200), nullable=False)
    year = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', year={self.year})"
