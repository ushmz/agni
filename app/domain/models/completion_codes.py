from infra.alchemy import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class CompletionCodes(Base):
    __tablename__ = "completion_codes"

    id = Column(
        Integer,
        index=True,
        primary_key=True,
        comment="Identification for internal process",
    )

    completion_codes = Column(String, comment="Completion code for each user")

    created_at = Column(
        DateTime, server_default=func.now(), comment="Created timestamp"
    )

    user = relationship("User")
