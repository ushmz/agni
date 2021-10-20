from sqlalchemy.sql.schema import ForeignKey
from infra.alchemy import Base
from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import relationship


class CompletionCodes(Base):
    __tablename__ = "completion_codes"

    id = Column(
        Integer,
        index=True,
        primary_key=True,
        comment="Identification for internal process",
    )

    user_id = Column(Integer, ForeignKey("users.id"))

    completion_code = Column(Integer, comment="Completion code for each user")

    created_at = Column(
        DateTime, server_default=func.now(), comment="Created timestamp"
    )

    user = relationship("User", back_populates="completion_code")
