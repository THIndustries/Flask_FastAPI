# main.py
from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise
from schemas import UserCreate, UserOut, ProductCreate, ProductOut, OrderCreate, OrderOut
from crud import create_user, get_user  # Импортируйте другие CRUD операции

app = FastAPI()

@app.post("/users/", response_model=UserOut)
async def create_user_endpoint(user: UserCreate):
    return await create_user(user)

@app.get("/users/{user_id}", response_model=UserOut)
async def get_user_endpoint(user_id: int):
    user = await get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Аналогично добавить маршруты для Product и Order

# Настройка Tortoise ORM
register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == '__main__':
    app.run()
