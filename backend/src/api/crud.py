import json

from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import Depends, Body

from src.db.base import Author, Book
from src.db.session import get_db
from src.api.create_app import app


@app.get("/api")
def root():
    return {'message': 'Hello! This is an application Authors and Books.'}


@app.get("/api/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    if books == []:
        return JSONResponse(status_code=404, content={"error": "The books not found"})
    res = []
    for book in books:
        res.append({book.id: book.title})
    return res


@app.get("/api/books/{id}")
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if book == None:
        return JSONResponse(status_code=404, content={"error": "The book not found"})
    return {book.id: book.title}


@app.get("/api/authors")
def get_authors(db: Session = Depends(get_db)):
    authors = db.query(Author).all()
    if authors == []:
        return JSONResponse(status_code=404, content={"error": "The authors not found"})
    res = []
    for author in authors:
        res.append({author.id: author.name})
    return res


@app.get("/api/authors/{id}")
def get_author(id: int, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == id).first()
    if author == None:
        return JSONResponse(status_code=404, content={
            "error": "The author not found"})
    return {author.id: author.name}


@app.post("/api/books")
def add_book(data=Body(), db: Session = Depends(get_db)):
    title = json.loads(data).get('title')
    book = Book(title=title)
    all_authors = db.query(Author).all()
    if not all_authors:
        return JSONResponse(status_code=404, content={
            "error": "Database dosn't contain any authors. "
            "Please add at least one author in database."})
    authors = json.loads(data).get('authors')
    if not authors:
        return JSONResponse(status_code=404, content={
            "error": "Authors aren't mentioned. "
            "Please mention at least one author."})
    for author in authors:
        book.authors.append(db.query(Author).filter(
            Author.id == author).first())
    db.add(book)
    db.commit()
    db.refresh(book)
    return [book] if book.authors else book


@app.post("/api/authors")
def add_author(data=Body(), db: Session = Depends(get_db)):
    name = json.loads(data).get('name')
    author = Author(name=name)
    books = json.loads(data).get('books')
    if books:
        for book in books:
            author.books.append(
                db.query(Book).filter(Book.id == book).first())
    db.add(author)
    db.commit()
    db.refresh(author)
    return [author, author.books] if books else author


@app.put("/api/books")
def change_book(data=Body(), db: Session = Depends(get_db)):
    id = json.loads(data).get('id')
    title = json.loads(data).get('title')
    book = db.query(Book).filter(Book.id == id).first()
    if book == None:
        return JSONResponse(status_code=404, content={"error": "The book not found"})
    book.title = title
    book_authors = {author.id for author in book.authors}
    authors_append = json.loads(data).get('authors_append')
    authors_exclude = json.loads(data).get('authors_exclude')
    if authors_append:
        for author in authors_append:
            if set(authors_append).difference(book_authors):
                author = db.query(Author).filter(
                    Author.id == author).first()
                if author:
                    book.authors.append(author)
                else:
                    return JSONResponse(status_code=404, content={
                        "error": "Author not found."})
            else:
                return JSONResponse(status_code=404, content={
                    "error": "Author is already mentioned."})
    if authors_exclude:
        book_authors.difference_update(set(authors_exclude))
        if not book_authors:
            return JSONResponse(status_code=404, content={
                "error": "Forbidden to delete the last author."})
        for author in authors_exclude:
            try:
                book.authors.remove(db.query(Author).filter(
                    Author.id == author).first())
            except ValueError:
                return JSONResponse(
                    status_code=404,
                    content={"error":
                             "The excludeble author is "
                             "not in the list of the book's authors"})
    db.commit()
    db.refresh(book)
    return [book] if book.authors else book


@app.put("/api/authors")
def change_author(data=Body(), db: Session = Depends(get_db)):
    id = json.loads(data).get('id')
    name = json.loads(data).get('name')
    author = db.query(Author).filter(Author.id == id).first()
    if author == None:
        return JSONResponse(status_code=404, content={"error": "The author not found"})
    author.name = name
    books_append = json.loads(data).get('books_append')
    books_exclude = json.loads(data).get('books_exclude')
    if books_append:
        for book in books_append:
            author.books.append(
                db.query(Book).filter(Book.id == book).first())
    if books_exclude:
        for book in books_exclude:
            author.books.remove(
                db.query(Book).filter(Book.id == book).first())
    db.commit()
    db.refresh(author)
    return [author] if author.books else author


@app.delete("/api/books/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if book == None:
        return JSONResponse(status_code=404, content={"error": "The book not found"})
    db.delete(book)
    db.commit()
    return book


@app.delete("/api/authors/{id}")
def delete_author(id: int, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == id).first()
    if author == None:
        return JSONResponse(status_code=404, content={"error": "The author not found"})
    db.delete(author)
    db.commit()
    return author
