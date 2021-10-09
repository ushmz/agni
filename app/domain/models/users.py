from infra.alchemy import Base
from sqlalchemy import Column, Integer, String, DateTime, func


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        index=True,
        primary_key=True,
        comment="Identification for internal process",
    )

    uid = Column(String, comment="Id of external Croudsourcing service")

    created_at = Column(
        DateTime, server_default=func.now(), comment="Created timestamp"
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment="Updated timestamp; Update each time when update any data",
    )
