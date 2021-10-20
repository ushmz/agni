# from datetime import datetime
# from typing import cast
from infra.alchemy import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Identification for internal process",
    )

    external_id = Column(
        String(64),
        comment="Identification of external Croudsourcing service",
    )

    created_at = Column(
        DateTime,
        server_default=func.now(),
        comment="Inserted once at creation, and should not updated",
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment="Updated timestamp; Update each time when update any data",
    )

    completion_code = relationship(
        "CompletionCodes", back_populates="user", uselist=False
    )
