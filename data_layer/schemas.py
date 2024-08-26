import json
import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_serializer, field_validator
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


class ScoreAspects(MappedCamelCaseBaseModel):
    child_friendly: Optional[float] = None
    food: Optional[float] = None
    hygiene: Optional[float] = None
    location: Optional[float] = None
    pool: Optional[float] = None
    price_quality: Optional[float] = None
    room: Optional[float] = None
    service: Optional[float] = None


class AccommodationScores(MappedCamelCaseBaseModel):
    general_score: float
    score_aspects: ScoreAspects


class Review(MappedCamelCaseBaseModel):
    id: uuid.UUID
    accommodation_id: uuid.UUID

    created_at: datetime
    general_score: float

    score_aspects: ScoreAspects

    @field_validator("score_aspects", mode="before")
    def deserialize_score_aspects(cls, score_aspects: str):
        return json.loads(score_aspects)

    @field_serializer("score_aspects")
    def serialize_score_aspects(score_aspects: ScoreAspects):
        return score_aspects.model_dump_json()
