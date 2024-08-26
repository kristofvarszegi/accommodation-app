import json
import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_serializer, field_validator
from pydantic.alias_generators import to_camel

from data_layer.schema_utils import datetime_to_str


# TODO Write unit tests
class MappedCamelCaseBaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        from_attributes=True,
        populate_by_name=True,
        json_encoders={datetime: datetime_to_str},
    )


class Accommodation(MappedCamelCaseBaseModel):
    id: uuid.UUID

    default_price: int
    name: str
    popularity_score: float
    slug: str
    stars: int
    zoover_gold_award: bool


class ScoreAspects(MappedCamelCaseBaseModel):
    child_friendly: Optional[float] = None
    food: Optional[float] = None
    hygiene: Optional[float] = None
    location: Optional[float] = None
    pool: Optional[float] = None
    price_quality: Optional[float] = None
    room: Optional[float] = None
    service: Optional[float] = None


class Review(MappedCamelCaseBaseModel):
    id: uuid.UUID
    accommodation_id: uuid.UUID

    created_at: datetime
    general_score: float
    text: str
    title: Optional[str]
    zoover_review_id: int

    score_aspects: ScoreAspects

    # TODO Write unit test
    @field_validator("score_aspects", mode="before")
    def deserialize_score_aspects(cls, score_aspects: str):
        return json.loads(score_aspects)

    # TODO Write unit test
    @field_serializer("score_aspects")
    def serialize_score_aspects(score_aspects: ScoreAspects):
        return score_aspects.model_dump_json(exclude_none=True)
