from pydantic import field_serializer

from data_layer.schemas import MappedCamelCaseBaseModel, ScoreAspects


# TODO Maybe use in Review to resolve duplicate code
class AccommodationScores(MappedCamelCaseBaseModel):
    general_score: float
    score_aspects: ScoreAspects

    @field_serializer("score_aspects")
    def serialize_score_aspects(score_aspects: ScoreAspects):
        return ScoreAspects(
            **{
                aspect: score or 0.0
                for aspect, score in score_aspects.model_dump().items()
            }
        )
