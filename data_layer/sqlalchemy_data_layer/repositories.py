import uuid

from sqlalchemy.orm import Session

from data_layer import schemas
from data_layer.repositories import IAccommodationRepository, IReviewRepository
from data_layer.sqlalchemy_data_layer.database import session_factory
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
        session.add(SqlAlchemyReview(**review.model_dump()))

    @staticmethod
    def get_for_accommodation(
        session, accommodation_id: uuid.UUID
    ) -> list[schemas.Review]:
        reviews = (
            session.query(SqlAlchemyReview)
            .filter_by(accommodation_id=accommodation_id)
            .all()
        )
        reviews = [schemas.Review(**review.__dict__) for review in reviews]
        return reviews

    @staticmethod
    def get_one_review_for_accommodation(
        session: Session, accommodation_id: uuid.UUID
    ) -> schemas.Review:
        review = (
            session.query(SqlAlchemyReview)
            .filter_by(accommodation_id=accommodation_id)
            .first()
        )
        return None if review is None else schemas.Review(**review.__dict__)


def get_accommodation_repository():
    yield SqlAlchemyAccommodationRepository


def get_review_repository():
    yield SqlAlchemyReviewRepository
