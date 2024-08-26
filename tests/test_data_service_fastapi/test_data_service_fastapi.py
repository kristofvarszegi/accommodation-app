from http import HTTPStatus

from fastapi.testclient import TestClient

from data_layer.config import get_accommodation_repository, get_review_repository
from data_service_fastapi.main import app
from tests.conftest import MockAccommodationRepository, MockReviewRepository

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Accommodation Data API"}


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


def test_get_review():
    response = client.get(
        "/accommodations/c9b7158b-1b07-4941-82d1-9ef8221e649d/reviews/6f102399-70dd-4302-be62-8186bd3149f0"
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": "6f102399-70dd-4302-be62-8186bd3149f0",
        "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
        "createdAt": "2018-05-26T00:00:00.000Z",
        "generalScore": 8.0,
        "scoreAspects": "{}"
    }


def test_get_review_does_not_exist_for_accommodation():
    response = client.get(
        "/accommodations/c9b7158b-1b07-4941-82d1-9ef8221e649d/reviews/8d869865-9356-49a3-b33d-d635278a839d"
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()["detail"] == "No reviews found for accommodation"


def test_get_reviews_for_accommodation():
    response = client.get(
        "/accommodations/c9b7158b-1b07-4941-82d1-9ef8221e649d/reviews/"
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == [
        {
            "id": "2cf4abc9-7b7c-4876-8d85-965eebeca34d",
            "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
            "createdAt": "2018-05-07T00:00:00.000Z",
            "generalScore": 9,
            "scoreAspects": "{}"
        },
        {
            "id": "6f102399-70dd-4302-be62-8186bd3149f0",
            "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
            "createdAt": "2018-05-26T00:00:00.000Z",
            "generalScore": 8,
            "scoreAspects": "{}"
        },
        {
            "id": "695fdea1-83e1-4744-9415-aa3e39b79691",
            "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
            "createdAt": "2018-09-23T00:00:00.000Z",
            "generalScore": 8,
            "scoreAspects": "{}"
        },
        {
            "id": "774673fd-d3f8-471c-a914-66c2afc83e01",
            "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
            "createdAt": "2018-10-03T00:00:00.000Z",
            "generalScore": 9,
            "scoreAspects": "{}"
        },
        {
            "id": "f3fce35a-af4f-40c1-9bda-ce0add8cc888",
            "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
            "createdAt": "2019-09-25T00:00:00.000Z",
            "generalScore": 8,
            "scoreAspects": "{}"
        },
        {
            "id": "3f43180b-9834-46e7-aa8b-6ee56242289b",
            "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
            "createdAt": "2020-06-26T00:00:00.000Z",
            "generalScore": 7,
            "scoreAspects": "{}"
        },
        {
            "id": "114e099c-a4ee-4373-93f0-562e062666e2",
            "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
            "createdAt": "2022-11-02T00:00:00.000Z",
            "generalScore": 9,
            "scoreAspects": "{}"
        },
        {
            "id": "f24e821f-6e60-48b0-9101-d32c1e0520ff",
            "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
            "createdAt": "2023-01-06T00:00:00.000Z",
            "generalScore": 9,
            "scoreAspects": "{}"
        },
        {
            "id": "1f5ae0a4-ddf5-4f73-b57f-eee305034564",
            "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
            "createdAt": "2023-01-22T00:00:00.000Z",
            "generalScore": 8,
            "scoreAspects": "{}"
        },
    ]
