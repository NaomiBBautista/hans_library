from fastapi.encoders import jsonable_encoder
from models.category import Category as CategoryModel
from models.book import Book as BookModel

class CategoryService():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_categories(self):
        total_categories = self.db.query(CategoryModel).count()
        if total_categories > 0:
            result = self.db.query(CategoryModel).all()
            self.db.close()
            return jsonable_encoder(result), 200
        return {"message": "No Categories Saved"}, 404
        
    def get_by_id(self, id: int):
        result = self.db.query(CategoryModel).filter(CategoryModel.id == id).first()
        self.db.close()
        if not result:
            return {"message": "Category Not Found"}, 404
        return jsonable_encoder(result), 200
    
    def create_category(self, newName: str):
        category_in_existence = self.db.query(CategoryModel).filter(CategoryModel.name == newName).first()
        if category_in_existence:
                return {"message": "Category Already Exists"}, 406
        
        new_category = CategoryModel(name=newName)
        self.db.add(new_category)
        self.db.commit()
        self.db.close()
        return {"message": "Category Succesfully Created"}, 200
    
    def update_category(self, id: int, newName: str):
        category_found = self.db.query(CategoryModel).filter(CategoryModel.id == id).first()
        if not category_found:
            return {"message": "Category Not Found"}, 404

        category_found.name = newName
        self.db.commit()
        self.db.close()
        return {"message": "Category Succesfully Updated"}, 200
    
    def delete_category(self, id: int):
        category_found = self.db.query(CategoryModel).filter(CategoryModel.id == id).first()
        if not category_found:
            return {"message": "Category Not Found"}, 404
        
        books_category = self.db.query(BookModel).filter(BookModel.id_category == category_found.id).first()
        if books_category:
            return {"message": "Category In Use"}, 406
        
        self.db.delete(category_found)
        self.db.commit()
        self.db.close()
        return {"message": "Category Succesfully Deleted"}, 200