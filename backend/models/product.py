from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None