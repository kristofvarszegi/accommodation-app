import uuid

from fastapi import Depends, FastAPI

from data_layer.config import create_session, get_review_repository
from data_layer.repositories import IReviewRepository
from scoring import schemas
from scoring.accommodation_scores import calculate_accommodation_scores

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Accommodation Scoring API"}


@app.get(
    "/accommodations/{accommodation_id}/scores/",
    response_model=schemas.AccommodationScores,
)
def get_accommodation_scores(
    accommodation_id: uuid.UUID,
    session=Depends(create_session),
    repository: IReviewRepository = Depends(get_review_repository),
):
    reviews = repository.list_for_accommodation(session, accommodation_id)
    if len(reviews) == 0:
        return schemas.AccommodationScores(
            general_score=0.0, score_aspects=schemas.ScoreAspects()
        )

    accommodation_scores = calculate_accommodation_scores(reviews)
    return accommodation_scores
