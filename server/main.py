from fastapi import FastAPI
from middleware.error_handlers import register_exception_handlers
from routes import users, user_interactions
from routes import websocket
import models

app = FastAPI()

app.include_router(users.router, prefix="/api")
app.include_router(user_interactions.router, prefix="/api")

app.include_router(websocket.router)

register_exception_handlers(app)
