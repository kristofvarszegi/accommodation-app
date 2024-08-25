import uuid
from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException

from data_layer import schemas
from data_layer.config import create_session, get_review_repository
from data_layer.repositories import IReviewRepository
from scoring.accommodation_ratings import calculate_accommodation_scores

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
        # TODO Rather just zero
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="No reviews found for accommodation",
        )

    accommodation_scores = calculate_accommodation_scores(reviews)
    return accommodation_scores
