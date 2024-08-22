import uuid
from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException

from data_layer import schemas
from data_layer.config import create_session, get_review_repository
from data_layer.repositories import IReviewRepository
from scoring.accommodation_ratings import calculate_accommodation_ratings

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Accommodation Scoring API"}


# TODO separate endpoint for each, or one endpoint calculating and returning all, or one endpoint for the general score
# and one returning all sub-scores?
# TODO As for the formula, ln(25 - (month current - month review)), does "month current - month review" mean that first we floor the current date floored to months (i.e. mapping its day value to 1), we floor the review's date to months, then substract the latter floored date from the former floored date? So, if the current date is January this year, but the review is from February last year, the result of "month current - month review" should be 11 and not -1, correct?
# TODO If we are in April 2023, a review created in May 2021 enters the calculation with its own weight, correct?
# TODO Score precision?
# TODO What to return if no review?
# TODO The 2-year age threshold should also be taken based on month-level precision (i.e. not day-level precision)?
# TODO In what timezone are the review datetimes specified?
# TODO For ln(1.77) I am getting 0.57 as opposed to 0.56 written in the assignment document
@app.get(
    "/accommodations/{accommodation_id}/general-score/",
    response_model=schemas.AccommodationRatings,
)
def get_accommodation_ratings(
    accommodation_id: uuid.UUID,
    session=Depends(create_session),
    repository: IReviewRepository = Depends(get_review_repository),
):
    reviews = repository.list_for_accommodation(session, accommodation_id)
    if len(reviews) == 0:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="No reviews found for accommodation",
        )

    accommodation_ratings = calculate_accommodation_ratings(reviews)
    return accommodation_ratings
