from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    # You might not need to create a user directly yet
    pass


class UserResponse(UserBase):
    pass
