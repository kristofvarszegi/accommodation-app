import abc
import uuid
from data_layer import models


class IAccommodationRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, accommodation: models.Accommodation):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, accommodation_id: uuid.UUID) -> models.Accommodation:
        raise NotImplementedError


class IReviewRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, review: models.Review):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, review_id: uuid.UUID) -> models.Review:
        raise NotImplementedError
