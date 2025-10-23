from uuid import UUID
from datetime import datetime, timedelta
from typing import Optional, List
from schemas.base import SchemaBase
from enums.interaction_types import InteractionType


class UserInteractionBase(SchemaBase):
    video_url: Optional[str]
    interaction_type: InteractionType
    watch_duration: Optional[timedelta]
    tags: Optional[List[str]] = None


class UserInteractionCreate(UserInteractionBase):
    user_id: UUID


class UserInteractionResponse(UserInteractionBase):
    id: UUID
    user_id: UUID
    created_at: datetime
