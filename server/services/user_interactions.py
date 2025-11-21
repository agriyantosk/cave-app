from models.user_interactions import UserInteraction
from sqlalchemy.ext.asyncio import AsyncSession
from utils.response import success_response
from schemas.user_interactions import UserInteractionCreate, UserInteractionResponse
from sqlalchemy import select, func


async def insert_user_interaction(db: AsyncSession, user_data: UserInteractionCreate):
    user_interaction = UserInteraction()
    db.add(user_interaction)
    await db.commit()
    await db.refresh(user_interaction)
    return success_response(UserInteractionResponse.model_validate(user_interaction), "User created successfully", 201)


async def count_user_interaction(db: AsyncSession, user_id: str) -> int:
    result = await db.execute(
        select(func.count()).select_from(UserInteraction).where(
            UserInteraction.user_id == user_id)
    )
    return result.scalar()
