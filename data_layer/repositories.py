import abc
import uuid
from typing import Optional

from data_layer import schemas


class IAccommodationRepository(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def add(session, accommodation: schemas.Accommodation):
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def get(session, accommodation_id: uuid.UUID) -> schemas.Accommodation:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def list(session, skip: int, limit: int) -> list[schemas.Accommodation]:
        raise NotImplementedError


class IReviewRepository(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def add(session, review: schemas.Review):
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def get(session, review_id: uuid.UUID) -> Optional[schemas.Review]:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def list_for_accommodation(
        session, accommodation_id: uuid.UUID
    ) -> list[schemas.Review]:
        raise NotImplementedError
