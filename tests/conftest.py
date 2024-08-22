import uuid
from http import HTTPStatus

from fastapi import HTTPException

from data_layer import schemas
from data_layer.repositories import IAccommodationRepository, IReviewRepository


class MockAccommodationRepository(IAccommodationRepository):
    @staticmethod
    def add(session, accommodation: schemas.Accommodation):
        raise NotImplementedError

    @staticmethod
    def get(session, accommodation_id: uuid.UUID) -> schemas.Accommodation:
        if accommodation_id == uuid.UUID("f4fec2d6-61af-4bfe-ae9f-2ec6881229cb"):
            return schemas.Accommodation(
                id="f4fec2d6-61af-4bfe-ae9f-2ec6881229cb", name="Dummy Hotel 2"
            )
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="Accommodation not found"
            )

    @staticmethod
    def list(session, skip: int, limit: int) -> list[schemas.Accommodation]:
        return [
            schemas.Accommodation(
                id="c9b7158b-1b07-4941-82d1-9ef8221e649d", name="Dummy Hotel 1"
            ),
            schemas.Accommodation(
                id="f4fec2d6-61af-4bfe-ae9f-2ec6881229cb", name="Dummy Hotel 2"
            ),
        ]


class MockReviewRepository(IReviewRepository):
    ACCOMMODATION_1_ID = "c9b7158b-1b07-4941-82d1-9ef8221e649d"
    REVIEWS = [
        schemas.Review(
            id="2cf4abc9-7b7c-4876-8d85-965eebeca34d",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2018-05-07T00:00:00.000Z",
            general_score=9.0,
        ),
        schemas.Review(
            id="6f102399-70dd-4302-be62-8186bd3149f0",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2018-05-26T00:00:00.000Z",
            general_score=8.0,
        ),
        schemas.Review(
            id="695fdea1-83e1-4744-9415-aa3e39b79691",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2018-09-23T00:00:00.000Z",
            general_score=8.0,
        ),
        schemas.Review(
            id="774673fd-d3f8-471c-a914-66c2afc83e01",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2018-10-03T00:00:00.000Z",
            general_score=9.0,
        ),
        schemas.Review(
            id="f3fce35a-af4f-40c1-9bda-ce0add8cc888",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2019-09-25T00:00:00.000Z",
            general_score=8.0,
        ),
        schemas.Review(
            id="3f43180b-9834-46e7-aa8b-6ee56242289b",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2020-06-26T00:00:00.000Z",
            general_score=7.0,
        ),
        schemas.Review(
            id="114e099c-a4ee-4373-93f0-562e062666e2",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2022-11-02T00:00:00.000Z",
            general_score=9.0,
        ),
        schemas.Review(
            id="f24e821f-6e60-48b0-9101-d32c1e0520ff",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2023-01-06T00:00:00.000Z",
            general_score=9.0,
        ),
        schemas.Review(
            id="1f5ae0a4-ddf5-4f73-b57f-eee305034564",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2023-01-22T00:00:00.000Z",
            general_score=8.0,
        ),
    ]

    @staticmethod
    def add(session, review: schemas.Review):
        raise NotImplementedError

    @staticmethod
    def list_for_accommodation(
        session, accommodation_id: uuid.UUID
    ) -> list[schemas.Review]:
        if accommodation_id == uuid.UUID(MockReviewRepository.ACCOMMODATION_1_ID):
            return MockReviewRepository.REVIEWS
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="No reviews found for accommodation",
            )

    @staticmethod
    def get(session, review_id: uuid.UUID) -> schemas.Review:
        for review in MockReviewRepository.REVIEWS:
            if review.id == review_id:
                return review
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="No reviews found for accommodation",
        )
