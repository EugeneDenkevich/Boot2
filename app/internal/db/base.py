from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, String, ForeignKey, Integer


# SQLALCHEMY_DATABASE_URL = "sqlite:///./authors_books.db"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://example:example@db:5432/authors_books"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
#                        "check_same_thread": False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()


class Author(Base):
    __tablename__ = "author"
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", secondary="author_book",
                         back_populates="authors")

    def __repr__(self):
        return f"<Author: {self.name}>"


class Book(Base):
    __tablename__ = "book"
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)
    title = Column(String)
    authors = relationship(
        "Author", secondary="author_book", back_populates="books")

    def __repr__(self):
        return f"<Book: {self.title}>"


class AuthorBook(Base):
    __tablename__ = 'author_book'
    __allow_unmapped__ = True

    author_id = Column(Integer, ForeignKey('author.id'), primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)


def create_db():
    global Base
    Base.metadata.create_all(bind=engine)


SessionLocal = sessionmaker(autoflush=False, bind=engine)
