from fastapi.encoders import jsonable_encoder
from models.book import Book as BookModel
from schemas.book import Book
from models.category import Category as CategoryModel
from sqlalchemy.orm import joinedload

class BookService():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_books(self):
        total_books = self.db.query(BookModel).count()
        if total_books > 0:
            result = self.db.query(BookModel).options(joinedload(BookModel.category)).all()
            self.db.close()
            return jsonable_encoder(result), 200
        return {"message": "No Books Saved"}, 404
    
    def get_by_code(self, code: int):
        result = self.db.query(BookModel).filter(BookModel.code == code).options(joinedload(BookModel.category)).first()
        self.db.close()
        if not result:
            return {"message": "Book Not Found"}, 404
        return jsonable_encoder(result), 200
    
    def get_by_category(self, category: str):
        category_found = self.db.query(CategoryModel).filter(CategoryModel.name == category).first()
        if not category_found:
            return {"message": "Category Does Not Exist"}, 404
        
        result = self.db.query(BookModel).filter(BookModel.category == category_found).options(joinedload(BookModel.category)).all()
        self.db.close()
        if not result:
            return {"message": "No Books In This Category"}, 404
        return jsonable_encoder(result), 200
    
    def create_book(self, book: Book):
        result = self.db.query(CategoryModel).filter(CategoryModel.name == book.category).first()
        if not result:
            return {"message": "Category Does Not Exist"}, 406
        
        book.category = result
        new_book = BookModel(**book.model_dump())
        self.db.add(new_book)
        self.db.commit()
        self.db.close() 
        return {"message": "Book Succesfully Created"}, 200
    
    def update_book(self, code: int, book_updated: Book):
        result = self.db.query(BookModel).filter(BookModel.code == code).first()
        if not result:
            return {"message": "Book Not Found"}, 404

        category_found = self.db.query(CategoryModel).filter(CategoryModel.name == book_updated.category).first()
        if not category_found:
            return {"message": "Category Not Found"}, 404 
        
        result.title = book_updated.title
        result.author = book_updated.author
        result.year = book_updated.year
        result.pages = book_updated.pages
        result.category = category_found
        self.db.commit()
        self.db.close()
        return {"message": "Book Succesfully Updated"}, 200
    
    def delete_book(self, code: int):
        result = self.db.query(BookModel).filter(BookModel.code == code).first()
        if not result:
            return {"message": "Book Not Found"}, 404
        self.db.delete(result)
        self.db.commit()
        self.db.close()
        return {"message": "Book Succesfully Deleted"}, 200