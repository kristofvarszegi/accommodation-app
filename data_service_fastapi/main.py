import uuid
from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException

from data_layer import schemas
from data_layer.config import (
    create_session,
    get_accommodation_repository,
    get_review_repository,
)
from data_layer.repositories import IAccommodationRepository, IReviewRepository

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Accommodation Data API"}


@app.get("/accommodations/", response_model=list[schemas.Accommodation])
def list_accommodations(
    skip: int = 0,
    limit: int = 100,
    session=Depends(create_session),
    repository: IAccommodationRepository = Depends(get_accommodation_repository),
):
    accommodations = repository.list(session, skip=skip, limit=limit)
    return accommodations


@app.get("/accommodations/{accommodation_id}/", response_model=schemas.Accommodation)
def get_accommodation(
    accommodation_id: uuid.UUID,
    session=Depends(create_session),
    repository: IAccommodationRepository = Depends(get_accommodation_repository),
):
    accommodation = repository.get(session, accommodation_id)
    if accommodation is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Accommodation not found"
        )
    return accommodation


@app.get(
    "/accommodations/{accommodation_id}/reviews/", response_model=list[schemas.Review]
)
def get_reviews_for_accommodation(
    accommodation_id: uuid.UUID,
    session=Depends(create_session),
    repository: IReviewRepository = Depends(get_review_repository),
):
    # TODO Raise 404 if the accommodation does not exist & unit test

    reviews = repository.list_for_accommodation(session, accommodation_id)
    if len(reviews) == 0:  # TODO Test
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="No reviews found for accommodation",
        )
    return reviews


@app.get(
    "/accommodations/{accommodation_id}/reviews/{review_id}",
    response_model=schemas.Review,
)
def get_review(
    accommodation_id: uuid.UUID,
    review_id: uuid.UUID,
    session=Depends(create_session),
    repository: IReviewRepository = Depends(get_review_repository),
):
    # TODO Raise 404 if the accommodation does not exist & unit test

    review = repository.get(session, review_id)

    if review is None:  # TODO Test
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Review not found")

    if review.accommodation_id != accommodation_id:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Review not found for accommodation",
        )

    return review
