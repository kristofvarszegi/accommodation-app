import json
import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

from data_layer import schemas
from data_layer.sqlalchemy_data_layer.constants import (
    ACCOMMODATIONS_TABLE_NAME,
    REVIEWS_TABLE_NAME,
)

Base = declarative_base()


class SqlAlchemyAccommodation(Base):
    __tablename__ = ACCOMMODATIONS_TABLE_NAME

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)

    default_price: Mapped[int]
    name: Mapped[str]
    popularity_score: Mapped[float]
    slug: Mapped[str]
    stars: Mapped[int]
    zoover_gold_award: Mapped[bool]

    reviews = relationship("SqlAlchemyReview")


class SqlAlchemyReview(Base):
    __tablename__ = REVIEWS_TABLE_NAME

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    accommodation_id: Mapped[UUID] = mapped_column(
        ForeignKey(f"{ACCOMMODATIONS_TABLE_NAME}.id")
    )

    created_at: Mapped[datetime]
    general_score: Mapped[float]
    text: Mapped[str]
    title: Mapped[Optional[str]]
    zoover_review_id: Mapped[int]

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

    # TODO Write unit test
    def to_schema(self) -> schemas.Review:
        return schemas.Review(
            id=self.id,
            accommodation_id=self.accommodation_id,
            created_at=self.created_at,
            general_score=self.general_score,
            text=self.text,
            title=self.title,
            zoover_review_id=self.zoover_review_id,
            score_aspects=json.dumps(  # TODO Using deserializer
                dict(
                    childFriendly=self.child_friendly,
                    food=self.food,
                    hygiene=self.hygiene,
                    location=self.location,
                    pool=self.pool,
                    priceQuality=self.price_quality,
                    room=self.room,
                    service=self.service,
                )
            ),
        )
