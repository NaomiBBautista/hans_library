from fastapi import APIRouter
from fastapi import Path, Query, Depends, Body
from fastapi.responses import JSONResponse
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from services.category import CategoryService

category_router = APIRouter()

# Get All Categories
@category_router.get('/categories', tags=['Categories'], status_code=200)
def getCategories() -> JSONResponse:
    db = Session()
    result, status = CategoryService(db).get_categories()
    return JSONResponse(content=result, status_code=status)
    
# Get Category By Code
@category_router.get('/categories/{id}', tags=['Categories'], status_code=200)
def getCategoryById(id: int = Path(ge=1)) -> JSONResponse:
    db = Session()
    result, status = CategoryService(db).get_by_id(id)
    return JSONResponse(content=result, status_code=status)

# Create New Category
@category_router.post('/categories', tags=['Categories'], status_code=200)
def createCategory(newName: str = Body(min_length=1, max_length=20, default="Category Name")) -> JSONResponse:
    db = Session()
    result, status = CategoryService(db).create_category(newName)
    return JSONResponse(content=result, status_code=status)
    
# Update Category
@category_router.put('/categories/{id}', tags=['Categories'], status_code=200)
def updateCategory(id: int = Path(ge=1), newName: str = Body(min_length=1, max_length=20, default="New Name")) -> JSONResponse:
    db = Session()
    result, status = CategoryService(db).update_category(id, newName)
    return JSONResponse(content=result, status_code=status)

# Delete Category
@category_router.delete('/categories/{id}', tags=['Categories'], status_code=200)
def deleteCategory(id: int = Path(ge=1)) -> JSONResponse:
    db = Session()
    result, status = CategoryService(db).delete_category(id)
    return JSONResponse(content=result, status_code=status)