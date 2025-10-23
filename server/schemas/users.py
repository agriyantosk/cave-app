from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    id: UUID
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class UserCreate(BaseModel):
    pass


class UserResponse(UserBase):
    pass
