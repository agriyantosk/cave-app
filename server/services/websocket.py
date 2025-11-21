from fastapi import WebSocket
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user_interactions import UserInteractionResponse
from services import users, devices, user_interactions
from schemas import UserCreate, DeviceCreate
from uuid import UUID as UUIDType


async def handle_initial_connection(websocket: WebSocket, db: AsyncSession, payload: dict):
    from uuid import UUID

    device_id = payload.get("device_id")
    user = None
    device = None

    # Case 1: No device_id sent — register new user + device
    if not device_id:
        user = await users.create_user(db, UserCreate())
        device = await devices.create_device(db, DeviceCreate(user_id=user.id))
        await websocket.send_json({
            "event": "registered",
            "data": {
                "user_id": str(user.id),
                "device_id": str(device.id),
            }
        })
        return

    # Case 2: device_id sent — try to find it
    device = await devices.get_device_by_id(db, device_id)

    if device:
        # Device exists — check if it has a user
        if device.user_id:
            await websocket.send_json({
                "event": "already_registered",
                "data": {
                    "user_id": str(device.user_id),
                    "device_id": str(device.id),
                }
            })
        else:
            # Device found but has no user → create one and assign
            user = await users.create_user(db, UserCreate())
            device.user_id = user.id
            await db.commit()
            await db.refresh(device)

            await websocket.send_json({
                "event": "user_assigned",
                "data": {
                    "user_id": str(user.id),
                    "device_id": str(device.id),
                }
            })

    else:
        # Device not found in DB → create it using the provided device_id
        try:
            # Validate UUID format
            UUID(device_id)
        except ValueError:
            await websocket.send_json({
                "event": "error",
                "message": "Invalid device_id format"
            })
            return

        user = await users.create_user(db, UserCreate())
        device = await devices.create_device(
            db,
            # 👈 force-create with given ID
            DeviceCreate(id=device_id, user_id=user.id)
        )

        await websocket.send_json({
            "event": "device_reinserted",
            "data": {
                "user_id": str(user.id),
                "device_id": str(device.id),
            }
        })


async def handle_user_interaction(websocket: WebSocket, db: AsyncSession, payload: dict):
    try:
        user_id = payload.get("user_id")
        UUIDType(user_id)

        user = await users.get_user_by_id(db, user_id)

        if not user:
            await websocket.send_json({
                "event": "error",
                "message": "user not found!"
            })
            return

        interaction = await user_interactions.insert_user_interaction(db, payload)
        await websocket.send_json({
            "event": "interaction_saved",
            "data": UserInteractionResponse.model_validate(interaction).model_dump()
        })

        # interaction_count = await user_interactions.count_user_interaction(db, user_id)

        # steps = interaction_count % 5
        # if steps == 0:
        # spin up puppeteer to get recoms
        # else:
        #     return

    except Exception as e:
        await websocket.send_json({
            "event": "error",
            "message": "failed to insert user interaction"
        })
