from fastapi import APIRouter, WebSocket
from websocket import conection_handler

router = APIRouter()


@router.websocket("/ws")
async def extension_socket(websocket: WebSocket):
    await conection_handler.handle_websocket_connection(websocket)
