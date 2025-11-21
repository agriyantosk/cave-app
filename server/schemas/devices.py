from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class DeviceBase(BaseModel):
    id: UUID
    user_id: UUID

    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class DeviceCreate(BaseModel):
    user_id: UUID


class DeviceResponse(DeviceBase):
    pass
