import uuid

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class Accommodation(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True
    )

    id: uuid.UUID
    name: str


class Review(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True
    )

    id: uuid.UUID
    general_score: float
    # TODO Sub-scores, rather as a "scores" table

    accommodation_id: uuid.UUID
