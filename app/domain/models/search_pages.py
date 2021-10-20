from infra.alchemy import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class SearchPages(Base):
    __tablename__ = "search_pages"

    id = Column(
        Integer,
        index=True,
        primary_key=True,
        comment="Identification for internal process",
    )

    title = Column(String, comment="Title of each page")

    url = Column(String, comment="URL of each page")

    snippet = Column(String, comment="Snippet of each page")

    created_at = Column(
        DateTime, server_default=func.now(), comment="Created timestamp"
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment="Updated timestamp; Update each time when update any data",
    )

    task = relationship("Task")
