from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from services import users
from schemas.users import UserCreate

router = APIRouter()


@router.post("/user")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await users.create_user(db, user)
