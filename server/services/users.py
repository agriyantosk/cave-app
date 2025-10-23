from models.users import User
from sqlalchemy.ext.asyncio import AsyncSession
from utils.response import success_response, error_response
from schemas.users import UserCreate, UserResponse


async def create_user(db: AsyncSession, user_data: UserCreate):
    user = User()
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return success_response(UserResponse.model_validate(user), "User created successfully", 201)
