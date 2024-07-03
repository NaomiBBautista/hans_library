from schemas.user import User
from models.user import User as UserModel
from utils.jwt_manager import create_token
from sqlalchemy import and_

class UserService():
    def __init__(self, db) -> None:
        self.db = db
        
    def login(self, user: User):
        result = self.db.query(UserModel).filter(and_(UserModel.email == user.email, UserModel.password == user.password)).first()
        self.db.close()
        
        if not result:
            return {"message": "Invalid User"}, 400
        token:str = create_token(dict(user))
        return token, 200
    
    def sing_up_user(self, user: User):
        new_user = UserModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()    
        self.db.close()
        return {"message": "User Succesfully Created"}, 200