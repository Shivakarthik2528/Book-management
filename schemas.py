from pydantic import BaseModel, 

class BookCreate(BaseModel):
    title: str  
    author: str
    category: str
    price: float
    quantity: int