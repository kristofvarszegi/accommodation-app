import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

from data_layer.sqlalchemy_data_layer.constants import (
    ACCOMMODATIONS_TABLE_NAME,
    REVIEWS_TABLE_NAME,
)

Base = declarative_base()


class SqlAlchemyAccommodation(Base):
    __tablename__ = ACCOMMODATIONS_TABLE_NAME

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
    reviews = relationship("SqlAlchemyReview")


class SqlAlchemyReview(Base):
    __tablename__ = REVIEWS_TABLE_NAME

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    accommodation_id: Mapped[UUID] = mapped_column(
        ForeignKey(f"{ACCOMMODATIONS_TABLE_NAME}.id")
    )

    created_at: Mapped[datetime]
    general_score: Mapped[float]

    # The sub-scores are flattened so they are direct members of the model instead of a
    # "score_aspects" field. This makes the score lookup easier, but needs a DB
    # migration every time a new score aspect is introduced. An alternative could be a
    # separate "scores" table that has an "aspect" column.
    child_friendly: Mapped[Optional[float]]
    food: Mapped[Optional[float]]
    hygiene: Mapped[Optional[float]]
    location: Mapped[Optional[float]]
    pool: Mapped[Optional[float]]
    price_quality: Mapped[Optional[float]]
    room: Mapped[Optional[float]]
    service: Mapped[Optional[float]]
