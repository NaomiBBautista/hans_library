from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token
from config.database import SessionLocal
from models.user import User as UserModel
from sqlalchemy import and_

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        db = SessionLocal()
        try:
            auth = await super().__call__(request)
            data = validate_token(auth.credentials)
            valid_user = db.query(UserModel).filter(and_(UserModel.email == data['email'], UserModel.password == data['password'])).first()
            
            if not valid_user:
                raise HTTPException(detail="Invalid Token", status_code=403)
            return auth
        except Exception as e:
            raise HTTPException(detail="Invalid Token", status_code=401)
        finally:
            db.close()