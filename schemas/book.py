from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str = Field(min_length = 1, max_length = 30)
    author: str = Field(min_length = 1, max_length = 20)
    year: int = Field(le = 2024)
    category: str = Field(min_length = 1, max_length = 20)
    pages: int = Field(ge=1)
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "My book",
                "author": "Desc",
                "year": 2000,
                "category": "Action",
                "pages": 180
            }
        }