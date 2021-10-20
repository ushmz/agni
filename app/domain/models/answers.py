from infra.alchemy import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class Answers(Base):
    __tablename__ = "answers"

    id = Column(
        Integer,
        index=True,
        primary_key=True,
        comment="Identification for internal process",
    )

    answer = Column(String, comment="Answer text for task")

    reason = Column(String, comment="Reason text for task answer")

    created_at = Column(
        DateTime, server_default=func.now(), comment="Created timestamp"
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment="Updated timestamp; Update each time when update any data",
    )

    user = relationship("User")

    task = relationship("Task")

    condition = relationship("Condition")
