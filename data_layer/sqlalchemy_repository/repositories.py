# TODO Resolve duplication
import uuid

from sqlalchemy.orm import Session

from data_layer import models
from data_layer.repositories import IAccommodationRepository, IReviewRepository
from data_layer.sqlalchemy_repository.models import (
    SqlAlchemyAccommodation,
    SqlAlchemyReview,
)


# TODO Session via DI
class SqlAlchemyAccommodationRepository(IAccommodationRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, accommodation: models.Accommodation):
        self.session.add(SqlAlchemyAccommodation(**accommodation.model_dump()))

    def get(self, accommodation_id: uuid.UUID) -> models.Accommodation:
        return models.Accommodation(
            **self.session.query(SqlAlchemyAccommodation).get(accommodation_id).__dict__
        )


# TODO Session via DI
class SqlAlchemyReviewRepository(IReviewRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, review: models.Review):
        self.session.add(SqlAlchemyReview(**review.model_dump()))

    def get(self, review_id: uuid.UUID) -> models.Review:
        return models.Review(
            **self.session.query(SqlAlchemyReview).get(review_id).__dict__
        )
