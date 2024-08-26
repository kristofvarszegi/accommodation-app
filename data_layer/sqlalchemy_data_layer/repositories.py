import uuid
from typing import Optional

from sqlalchemy.orm import Session

from data_layer import schemas
from data_layer.repositories import IAccommodationRepository, IReviewRepository
from data_layer.sqlalchemy_data_layer.models import (
    SqlAlchemyAccommodation,
    SqlAlchemyReview,
)


class SqlAlchemyAccommodationRepository(IAccommodationRepository):
    @staticmethod
    def add(session: Session, accommodation: schemas.Accommodation):
        session.add(SqlAlchemyAccommodation(**accommodation.model_dump()))

    @staticmethod
    def get(session: Session, accommodation_id: uuid.UUID) -> schemas.Accommodation:
        return schemas.Accommodation(
            **session.query(SqlAlchemyAccommodation).get(accommodation_id).__dict__
        )

    @staticmethod
    def list(session: Session, skip: int, limit: int) -> list[schemas.Accommodation]:
        accommodations = (
            session.query(SqlAlchemyAccommodation).offset(skip).limit(limit).all()
        )
        accommodations = [
            schemas.Accommodation(**accommodation.__dict__)
            for accommodation in accommodations
        ]
        return accommodations


class SqlAlchemyReviewRepository(IReviewRepository):
    @staticmethod
    def add(session: Session, review: schemas.Review):
        fields = {
            key: value
            for key, value in review.model_dump().items()
            if key != "score_aspects"
        }
        fields.update(review.score_aspects.model_dump())
        session.add(SqlAlchemyReview(**fields))

    @staticmethod
    def get(session: Session, review_id: uuid.UUID) -> Optional[schemas.Review]:
        review = session.query(SqlAlchemyReview).filter_by(id=review_id).first()
        return None if review is None else review.to_schema()

    @staticmethod
    def list_for_accommodation(
        session, accommodation_id: uuid.UUID
    ) -> list[schemas.Review]:
        reviews = (
            session.query(SqlAlchemyReview)
            .filter_by(accommodation_id=accommodation_id)
            .all()
        )
        reviews = [review.to_schema() for review in reviews]
        return reviews


def get_accommodation_repository():
    yield SqlAlchemyAccommodationRepository


def get_review_repository():
    yield SqlAlchemyReviewRepository
