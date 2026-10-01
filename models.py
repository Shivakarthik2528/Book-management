from sqlalchemy import column, Integer, String, ForeignKey
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = column(Integer, primary_key=True, index=True)
    title = column(String)
    author = column(String)
    category = column(String)
    price = column(Float)
    quantity = column(Integer)

    user_id = column(Integer, ForeignKey("users.id"))