import uuid
from datetime import datetime

from sqlalchemy import UUID, Column, Float, ForeignKey
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
    # TODO Sub-scores, rather as a "scores" table
