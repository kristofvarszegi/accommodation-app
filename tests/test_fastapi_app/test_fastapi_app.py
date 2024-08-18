from http import HTTPStatus

from fastapi.testclient import TestClient

from data_layer.config import get_accommodation_repository, get_review_repository
from fastapi_app.main import app
from tests.conftest import MockAccommodationRepository, MockReviewRepository

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Accommodation API"}


# TODO Find the way to override "create_session" so the endpoint does not raise 422
app.dependency_overrides[get_accommodation_repository] = MockAccommodationRepository
app.dependency_overrides[get_review_repository] = MockReviewRepository


def test_list_accommodations():
    response = client.get("/accommodations/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == [
        {"id": "c9b7158b-1b07-4941-82d1-9ef8221e649d", "name": "Dummy Hotel 1"},
        {"id": "f4fec2d6-61af-4bfe-ae9f-2ec6881229cb", "name": "Dummy Hotel 2"},
    ]


def test_get_accommodation():
    response = client.get("/accommodations/f4fec2d6-61af-4bfe-ae9f-2ec6881229cb")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": "f4fec2d6-61af-4bfe-ae9f-2ec6881229cb",
        "name": "Dummy Hotel 2",
    }


def test_get_reviews_for_accommodation():
    response = client.get(
        "/accommodations/c9b7158b-1b07-4941-82d1-9ef8221e649d/reviews/"
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == [
        {
            "id": "2cf4abc9-7b7c-4876-8d85-965eebeca34d",
            "generalScore": 3.14,
            "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
        },
        {
            "id": "6f102399-70dd-4302-be62-8186bd3149f0",
            "generalScore": 3.15,
            "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
        },
    ]


def test_get_one_review_for_accommodation():
    response = client.get(
        "/accommodations/c9b7158b-1b07-4941-82d1-9ef8221e649d/one-review/"
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": "6f102399-70dd-4302-be62-8186bd3149f0",
        "generalScore": 3.15,
        "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
    }
