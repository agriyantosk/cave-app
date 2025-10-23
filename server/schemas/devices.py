from uuid import UUID
from datetime import datetime
from sqlalchemy import DateTime
from pydantic import BaseModel


class DeviceBase(BaseModel):
    id: UUID
    user_id: UUID

    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class DeviceCreate(BaseModel):
    pass


class DeviceResponse(DeviceBase):
    pass
