from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, SessionLocal, Base
from models import Book 
from schemas import BookCreate

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {
        "message": "Welcome to the Book Management API!"
    }

@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@app.post("/books")
def create_book(
    book_data: BookCreate, 
    db: Session = Depends(get_db)
    ):
    new_book = Book(
        title=book_data.title,
        author=book_data.author,
        category=book_data.category,
        price=book_data.price,
        quantity=book_data.quantity
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book