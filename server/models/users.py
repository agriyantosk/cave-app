from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from base import Base
from timestamp_mixin import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    user_interactions = relationship(
        "UserInteraction", back_populates="user", cascade="all, delete")
