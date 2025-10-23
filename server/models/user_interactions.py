from sqlalchemy import Enum, Text, Interval
from sqlalchemy import Column, DateTime, ARRAY, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from base import Base
from uuid import uuid4
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enums.interaction_types import InteractionType


class UserInteraction(Base):
    __tablename__ = "user_interactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    video_url = Column(Text)
    interaction_type = Column(Enum(InteractionType), nullable=False)
    watch_duration = Column(Interval, nullable=True)
    tags = Column(ARRAY(Text), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="user_interactions")