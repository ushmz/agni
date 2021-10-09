from infra.alchemy import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class TimeLog(Base):
    __tablename__ = "dwell_time_logs"

    id = Column(
        Integer,
        index=True,
        primary_key=True,
        comment="Identification for internal process",
    )

    dwell_time = Column(Integer, comment="Dwell time in search result page")

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


class ClickLog(Base):
    __tablename__ = "click_logs"

    id = Column(
        Integer,
        index=True,
        primary_key=True,
        comment="Identification for internal process",
    )

    dwell_time = Column(Integer, comment="Dwell time in search result page")

    url = Column(String, comment="Clicked page URL")

    referrer = Column(String, comment="Referrer of each click log")

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
