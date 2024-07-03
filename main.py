from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from middlewares.request_logger import RequestLogger
from routers.book import book_router
from routers.category import category_router
from routers.user import user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.title = "HANS LIBRARY"
app.version = "2.0"

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:5500",
    "http://157.230.222.10",
    "http://hans-library.com",
    "http://www.hans-library.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(ErrorHandler)
app.add_middleware(RequestLogger)
# app.include_router(user_router)
app.include_router(book_router)
app.include_router(category_router)

Base.metadata.create_all(bind=engine) 