from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.internal.db.base import Author, Book
from app.internal.db.session import get_db
from app.internal.models import author_book


router = APIRouter(prefix="/api")


@router.get(
    "/books", tags=["Books"], responses=author_book.get_books_responses
)
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    if books == []:
        return JSONResponse(
            status_code=404, content={"error": "The books not found"}
        )
    res = []
    for book in books:
        res.append(
            {"id": int(book.id), "title": book.title, "authors": book.authors}
        )
    return res


@router.get(
    "/books/{id}", tags=["Books"], responses=author_book.get_book_responses
)
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        return JSONResponse(
            status_code=404, content={"error": "The book not found"}
        )
    res = {"id": int(book.id), "title": book.title, "authors": book.authors}
    return res


@router.get(
    "/authors", tags=["Authors"], responses=author_book.get_authors_responses
)
def get_authors(db: Session = Depends(get_db)):
    authors = db.query(Author).all()
    if authors == []:
        return JSONResponse(
            status_code=404, content={"error": "The authors not found"}
        )
    res = []
    for author in authors:
        res.append(
            {"id": int(author.id), "name": author.name, "books": author.books}
        )
    return res


@router.get(
    "/authors/{id}",
    tags=["Authors"],
    responses=author_book.get_author_responses,
)
def get_author(id: int, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == id).first()
    if author is None:
        return JSONResponse(
            status_code=404, content={"error": "The author not found"}
        )
    res = {"id": int(author.id), "name": author.name, "books": author.books}
    return res


@router.post(
    "/books",
    tags=["Books"],
    responses={200: {"model": author_book.BookAddBaseModel}},
    description="Point the authors ids as integer numbers "
    "in authors=[] separate by , - You can't create "
    "book without at least one author.",
)
def add_book(
    data: author_book.BookAddBaseModel, db: Session = Depends(get_db)
):
    title = data.title
    book = Book(title=title)
    all_authors = db.query(Author).all()
    if not all_authors:
        return JSONResponse(
            status_code=404,
            content={
                "error": "Database dosn't contain any authors. "
                "Please add at least one author in database."
            },
        )
    authors = set(data.authors)
    if not authors:
        return JSONResponse(
            status_code=404,
            content={
                "error": "Authors aren't mentioned. "
                "Please mention at least one author."
            },
        )
    for author in authors:
        a = db.query(Author).filter(Author.id == author).first()
        if a:
            book.authors.append(a)
        else:
            return JSONResponse(
                status_code=404,
                content={"error": "Author in the list not faund"},
            )
    db.add(book)
    db.commit()
    db.refresh(book)
    book.authors
    return book


@router.post(
    "/authors",
    tags=["Authors"],
    responses={200: {"model": author_book.AuthorAddBaseModel}},
    description="Point the books ids as integer numbers "
    "in books=[] separate by , - You can create author "
    "without any books.",
)
def add_author(
    data: author_book.AuthorAddBaseModel, db: Session = Depends(get_db)
):
    name = data.name
    author = Author(name=name)
    books = set(data.books)
    if books:
        for book in books:
            b = db.query(Book).filter(Book.id == book).first()
            if b:
                author.books.append(b)
            else:
                return JSONResponse(
                    status_code=404,
                    content={"error": "Books in the list not faund"},
                )
    db.add(author)
    db.commit()
    db.refresh(author)
    author.books
    return author


@router.put(
    "/books",
    tags=["Books"],
    responses={
        200: {"model": author_book.BookChangeBaseModel},
    },
    description="Point the authors ids as integer numbers "
    "in authors_append=[] separate by , if you "
    "want to append authors.\n Point the authors "
    "ids as integer numbers in authors_exclude=[] "
    "separate by , if you want to exclude "
    "authors.",
)
def change_book(
    data: author_book.BookChangeBaseModel, db: Session = Depends(get_db)
):
    id = data.id
    title = data.title
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        return JSONResponse(
            status_code=404, content={"error": "The book not found"}
        )
    book.title = title
    book_authors = {author.id for author in book.authors}
    authors_append = set(data.authors_append)
    authors_exclude = set(data.authors_exclude)
    if authors_append:
        for author in authors_append:
            if author not in book_authors:
                author = db.query(Author).filter(Author.id == author).first()
                if author:
                    book.authors.append(author)
                else:
                    return JSONResponse(
                        status_code=404, content={"error": "Author not found."}
                    )
            else:
                return JSONResponse(
                    status_code=404,
                    content={"error": "Author is already mentioned."},
                )
    if authors_exclude:
        book_authors.difference_update(authors_exclude)
        if not book_authors:
            return JSONResponse(
                status_code=403,
                content={"error": "Forbidden to delete the last author."},
            )
        for author in authors_exclude:
            try:
                book.authors.remove(
                    db.query(Author).filter(Author.id == author).first()
                )
            except ValueError:
                return JSONResponse(
                    status_code=404,
                    content={
                        "error": "The excludeble author is "
                        "not in the list of the book's authors"
                    },
                )
    db.commit()
    db.refresh(book)
    book.authors
    return book


@router.put(
    "/authors",
    tags=["Authors"],
    responses={
        200: {"model": author_book.AuthorChangeBaseModel},
    },
    description="Point the books ids as integer numbers "
    "in books_append=[] separate by , if you "
    "want to append books.\n Point the books "
    "ids as integer numbers in books_exclude=[] "
    "separate by , if you want to exclude "
    "books.",
)
def change_author(
    data: author_book.AuthorChangeBaseModel, db: Session = Depends(get_db)
):
    id = data.id
    name = data.name
    author = db.query(Author).filter(Author.id == id).first()
    if author is None:
        return JSONResponse(
            status_code=404, content={"error": "The author not found"}
        )
    author.name = name
    author_books = {book.id for book in author.books}
    books_append = set(data.books_append)
    books_exclude = set(data.books_exclude)
    if books_append:
        for book in set(books_append):
            if book not in author_books:
                book = db.query(Book).filter(Book.id == book).first()
                if book:
                    author.books.append(book)
                else:
                    return JSONResponse(
                        status_code=404, content={"error": "Book not found."}
                    )
            else:
                return JSONResponse(
                    status_code=404,
                    content={"error": "Book is already in author's works."},
                )
    if books_exclude:
        for book in books_exclude:
            try:
                author.books.remove(
                    db.query(Book).filter(Book.id == book).first()
                )
            except ValueError:
                return JSONResponse(
                    status_code=404,
                    content={
                        "error": "The excludeble books are "
                        "not in the list of the author's books"
                    },
                )
    db.commit()
    db.refresh(author)
    return [author] if author.books else author


@router.delete(
    "/books/{id}", tags=["Books"], responses=author_book.delete_books_responses
)
def delete_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        return JSONResponse(
            status_code=404, content={"error": "The book not found"}
        )
    db.delete(book)
    db.commit()
    return book


@router.delete(
    "/authors/{id}",
    tags=["Authors"],
    responses=author_book.delete_authors_responses,
)
def delete_author(id: int, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == id).first()
    if author is None:
        return JSONResponse(
            status_code=404, content={"error": "The author not found"}
        )
    db.delete(author)
    db.commit()
    return author
