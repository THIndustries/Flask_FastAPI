# crud.py
from models import User, Product, Order
from schemas import UserCreate, ProductCreate, OrderCreate
from tortoise.transactions import in_transaction

async def create_user(user: UserCreate):
    async with in_transaction() as conn:
        user_obj = await User.create(**user.dict(), using_db=conn)
        return user_obj

async def get_user(user_id: int):
    return await User.get(id=user_id)

# Аналогично реализовать CRUD операции для Product и Order
