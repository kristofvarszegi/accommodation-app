from http import HTTPStatus

from fastapi.testclient import TestClient
from freezegun import freeze_time

from data_layer.config import get_review_repository
from scoring_service_fastapi.main import app
from tests.conftest import MockReviewRepository

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Accommodation Scoring API"}


# TODO Find the way to override "create_session" so the endpoint does not raise 422
app.dependency_overrides[get_review_repository] = MockReviewRepository


# TODO Also for the calculator function
@freeze_time("2023-04-01")
def test_get_accommodation_ratings():
    response = client.get(
        "/accommodations/c9b7158b-1b07-4941-82d1-9ef8221e649d/general-score"
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"generalScore": 8.63}


# TODO Rather for just the calculator function
@freeze_time("2100-01-01")
def test_get_accommodation_ratings_when_all_reviews_are_old():
    response = client.get(
        "/accommodations/c9b7158b-1b07-4941-82d1-9ef8221e649d/general-score"
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"generalScore": 8.33}


# TODO, Rather for just the calculator function
# def test_get_accommodation_ratings_when_no_reviews_are_old():
