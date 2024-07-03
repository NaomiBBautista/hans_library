from pydantic import BaseModel, Field

class Category(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Write category",
            }
        }