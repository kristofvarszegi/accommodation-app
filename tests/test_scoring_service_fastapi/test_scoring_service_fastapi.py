from http import HTTPStatus

from fastapi.testclient import TestClient
from freezegun import freeze_time

from data_layer.config import get_review_repository
from services.scoring_service_fastapi.main import app
from tests.conftest import MockReviewRepository

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Accommodation Scoring API"}


# TODO Find the way to override "create_session" so the endpoint does not raise 422
app.dependency_overrides[get_review_repository] = MockReviewRepository


@freeze_time("2023-04-01")
def test_get_scores():
    response = client.get(
        "/accommodations/c9b7158b-1b07-4941-82d1-9ef8221e649d/scores/"
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "generalScore": 8.63,
        "scoreAspects": {
            "childFriendly": 0.0,
            "food": 0.0,
            "hygiene": 0.0,
            "location": 0.0,
            "pool": 0.0,
            "priceQuality": 0.0,
            "room": 0.0,
            "service": 0.0,
        },
    }


def test_get_scores_returns_all_zeros_when_no_reviews():
    response = client.get(
        "/accommodations/f4fec2d6-61af-4bfe-ae9f-2ec6881229cb/scores/"
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "generalScore": 0.0,
        "scoreAspects": {
            "childFriendly": 0.0,
            "food": 0.0,
            "hygiene": 0.0,
            "location": 0.0,
            "pool": 0.0,
            "priceQuality": 0.0,
            "room": 0.0,
            "service": 0.0,
        },
    }
