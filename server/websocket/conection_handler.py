from fastapi import WebSocket
from database.session import AsyncSessionLocal
import services.websocket as websocket_services


async def handle_websocket_connection(websocket: WebSocket):
    await websocket.accept()
    db = AsyncSessionLocal()

    try:
        while True:
            data = await websocket.receive_json()
            event = data.get("event")
            payload = data.get("data")

            if event == "initial_connection":
                await websocket_services.handle_initial_connection(websocket, db, payload)

            elif event == "user_interaction":
                await websocket_services.handle_user_interaction(websocket, db, payload)

            else:
                await websocket.send_json({
                    "event": "error",
                    "message": f"Unknown event: {event}"
                })

    except Exception as e:
        await websocket.send_json({"event": "error", "message": str(e)})
        await websocket.close()
    finally:
        await db.close()
