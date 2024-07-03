from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from config.database import Session
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from middlewares.jwt_bearer import JWTBearer
from schemas.user import User
from services.user import UserService

user_router = APIRouter()
        
@user_router.post('/login', tags=['auth'], status_code=200)
def login(user: User) -> JSONResponse:
    db = Session()
    result, status = UserService(db).login(user)
    return JSONResponse(content=result, status_code=status)

@user_router.post('/singup', tags=['auth'], status_code=200, dependencies=[Depends(JWTBearer())])
def singUpUser(user: User) -> JSONResponse:
    db = Session()
    result, status = UserService(db).sing_up_user(user)
    return JSONResponse(content=result, status_code=status)