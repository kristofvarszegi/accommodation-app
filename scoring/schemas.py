from data_layer.schemas import MappedCamelCaseBaseModel, ScoreAspects


class AccommodationScores(MappedCamelCaseBaseModel):
    general_score: float
    score_aspects: ScoreAspects
