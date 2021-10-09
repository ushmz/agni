from infra.alchemy import Base
from sqlalchemy import Column, Integer, String, DateTime, func


class Task(Base):
    __tablename__ = "tasks"

    id = Column(
        Integer,
        index=True,
        primary_key=True,
        comment="Identification for internal process",
    )

    query = Column(String, comment="Search query for each task")

    title = Column(String, comment="Title of each task")

    description = Column(String, comment="Description of each task")

    search_url = Column(String, comment="Dummy URL path of each task")

    created_at = Column(
        DateTime, server_default=func.now(), comment="Created timestamp"
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment="Updated timestamp; Update each time when update any data",
    )
