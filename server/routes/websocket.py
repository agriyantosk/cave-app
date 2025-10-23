from fastapi import APIRouter, WebSocket
from services import websocket

router = APIRouter()


@router.websocket("/ws")
async def extension_socket(websocket: WebSocket):
    await websocket.handle_connection(websocket)
