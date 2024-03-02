from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    user_id: int
    product_id: int

class OrderOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: datetime
    status: str

    class Config:
        from_attributes = True
