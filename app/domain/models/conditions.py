from infra.alchemy import Base
from sqlalchemy import Column, Integer, String


class Condition(Base):
    __tablename__ = "conditions"

    id = Column(
        Integer,
        index=True,
        primary_key=True,
        comment="Identification for internal process",
    )

    condition = Column(String, comment="Detail condition name")
