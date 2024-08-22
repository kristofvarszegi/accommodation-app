import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from data_layer.schema_utils import datetime_to_str


class MappedCamelCaseBaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        from_attributes=True,
        populate_by_name=True,
        json_encoders={datetime: datetime_to_str},
    )


class Accommodation(MappedCamelCaseBaseModel):
    id: uuid.UUID
    name: str


class AccommodationRatings(MappedCamelCaseBaseModel):
    general_score: float

    # child_friendly: float
    # food: float
    # hygiene: float
    # location: float
    # pool: float
    # price_quality: float
    # room: float
    # service: float


class Review(MappedCamelCaseBaseModel):
    id: uuid.UUID
    accommodation_id: uuid.UUID

    created_at: datetime  # TODO Date directly?
    general_score: float
    # TODO Sub-scores, rather as a "scores" table
