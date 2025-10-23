from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.timestamp_mixin import TimestampMixin
from models.base import Base


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    user_interactions = relationship(
        "UserInteraction", back_populates="user", cascade="all, delete")
    devices = relationship("Device", back_populates="user")
