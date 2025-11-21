from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.devices import Device
from schemas.devices import DeviceCreate


async def create_device(db: AsyncSession, device_data: DeviceCreate):
    device = Device(**device_data.model_dump())
    db.add(device)
    await db.commit()
    await db.refresh(device)
    return device


async def get_device_by_id(db: AsyncSession, device_id: str):
    return await db.get(Device, device_id)
