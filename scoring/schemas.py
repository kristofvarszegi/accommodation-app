from pydantic import field_serializer
from pydantic.alias_generators import to_camel

from data_layer.schemas import MappedCamelCaseBaseModel, ScoreAspects


class AccommodationScores(MappedCamelCaseBaseModel):
    general_score: float
    score_aspects: ScoreAspects

    # TODO Write unit test
    @field_serializer("score_aspects")
    def serialize_score_aspects(score_aspects: ScoreAspects):
        return {
            to_camel(aspect): score or 0.0
            for aspect, score in score_aspects.model_dump().items()
        }
        # TODO Figure out why aspect does not automatically get converted to
        # camel case here
