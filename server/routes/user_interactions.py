from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from services import user_interactions
from schemas.user_interactions import UserInteractionCreate

router = APIRouter()


@router.post("/user-interaction")
async def create_user_interaction(
    interaction: UserInteractionCreate, 
    db: AsyncSession = Depends(get_db)
):
    return await user_interactions.create_user_interaction(db, interaction)
