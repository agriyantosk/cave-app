import json
from fastapi import WebSocket
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import AsyncSessionLocal
from services import users
from schemas.users import UserCreate


async def handle_connection(websocket: WebSocket):
    await websocket.accept()
    db: AsyncSession = AsyncSessionLocal()

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)

            event = message.get("event")
            payload = message.get("data")

            if event == "create_user":
                # You can customize what you pass to UserCreate
                user_create = UserCreate(**payload)  # empty for now
                user = await users.create_user(db, user_create)

                await websocket.send_text(json.dumps({
                    "event": "user_created",
                    # assuming your `success_response` returns dict
                    "data": user["data"]
                }))

            else:
                await websocket.send_text(json.dumps({
                    "event": "error",
                    "message": f"Unknown event: {event}"
                }))

    except Exception as e:
        await websocket.send_text(json.dumps({
            "event": "error",
            "message": str(e)
        }))
    finally:
        await db.close()
        await websocket.close()
