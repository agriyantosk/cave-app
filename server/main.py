from fastapi import FastAPI
from middleware.error_handlers import register_exception_handlers
from routes import users, user_interactions
import models

app = FastAPI()

app.include_router(users.router, prefix="/api")
app.include_router(user_interactions.router, prefix="/api")

register_exception_handlers(app)
