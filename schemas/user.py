from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "name@gmail.com",
                "password": "password",
            }
        }