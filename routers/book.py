from fastapi import APIRouter
from fastapi import Path, Query, Depends, Body
from fastapi.responses import JSONResponse
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from schemas.book import Book
from services.book import BookService

book_router = APIRouter()

# Get All Books
@book_router.get('/books', tags=['Books'], status_code=200)
def getBooks() -> JSONResponse:
    db = Session()
    result, status = BookService(db).get_books()
    return JSONResponse(content=result, status_code=status)
    
# Get Book By Code
@book_router.get('/books/{code}', tags=['Books'], status_code=200)
def getBookByCode(code: int = Path(ge=1, le=2000)) -> JSONResponse:
    db = Session()
    result, status = BookService(db).get_by_code(code)
    return JSONResponse(content=result, status_code=status)

# Get Books by Category
@book_router.get('/books_by_category/', tags=['Books'], status_code=200)
def getBooksByCategory(category: str = Query(...)) -> JSONResponse:
    db = Session()
    print(f"Category received: {category}")  # Asegúrate de que la categoría se recibe correctamente
    result, status = BookService(db).get_by_category(category)
    return JSONResponse(content=result, status_code=status)

# Create Book
@book_router.post('/books', tags=['Books'], status_code=200)
def createBook(book: Book = Body()) -> JSONResponse:
    db = Session()
    result, status = BookService(db).create_book(book)
    return JSONResponse(content=result, status_code=status)

# Update Book
@book_router.put('/books/{code}', tags=['Books'], status_code=200)
def updateBook(code: int = Path(ge=1, le=2000), book_updated: Book = Body()) -> JSONResponse:
    db = Session()
    result, status = BookService(db).update_book(code, book_updated)
    return JSONResponse(content=result, status_code=status)

# Delete Book
@book_router.delete('/books/{code}', tags=['Books'], status_code=200)
def deleteBook(code: int = Path(ge=1, le=2000)) -> JSONResponse:
    db = Session()
    result, status = BookService(db).delete_book(code)
    return JSONResponse(content=result, status_code=status)