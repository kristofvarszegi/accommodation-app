import uuid
from http import HTTPStatus

from fastapi import HTTPException

from data_layer import schemas
from data_layer.repositories import IAccommodationRepository, IReviewRepository


class MockAccommodationRepository(IAccommodationRepository):
    ACCOMMODATIONS = [
        schemas.Accommodation(
            id="c9b7158b-1b07-4941-82d1-9ef8221e649d",
            default_price=11000,
            name="Dummy Hotel 1",
            popularity_score=10.1,
            slug="dummy-hotel-1",
            stars=1,
            zoover_gold_award=False,
        ),
        schemas.Accommodation(
            id="f4fec2d6-61af-4bfe-ae9f-2ec6881229cb",
            default_price=22000,
            name="Dummy Hotel 2",
            popularity_score=20.2,
            slug="dummy-hotel-2",
            stars=2,
            zoover_gold_award=True,
        ),
    ]

    @staticmethod
    def add(session, accommodation: schemas.Accommodation):
        raise NotImplementedError

    @staticmethod
    def get(session, accommodation_id: uuid.UUID) -> schemas.Accommodation:
        for accommodation in MockAccommodationRepository.ACCOMMODATIONS:
            if accommodation.id == accommodation_id:
                return accommodation
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Accommodation not found"
        )

    @staticmethod
    def list(session, skip: int, limit: int) -> list[schemas.Accommodation]:
        return MockAccommodationRepository.ACCOMMODATIONS


class MockReviewRepository(IReviewRepository):
    ACCOMMODATION_1_ID = uuid.UUID("c9b7158b-1b07-4941-82d1-9ef8221e649d")
    REVIEWS = [
        schemas.Review(
            id="2cf4abc9-7b7c-4876-8d85-965eebeca34d",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2018-05-07T00:00:00.000Z",
            general_score=9.0,
            text="Dummy text 1",
            title="Dummy Title 1",
            zoover_review_id=1000001,
            score_aspects=schemas.ScoreAspects().model_dump_json(),
        ),
        schemas.Review(
            id="6f102399-70dd-4302-be62-8186bd3149f0",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2018-05-26T00:00:00.000Z",
            general_score=8.0,
            text="Dummy text 2",
            title="Dummy Title 2",
            zoover_review_id=2000002,
            score_aspects=schemas.ScoreAspects().model_dump_json(),
        ),
        schemas.Review(
            id="695fdea1-83e1-4744-9415-aa3e39b79691",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2018-09-23T00:00:00.000Z",
            general_score=8.0,
            text="Dummy text 3",
            title="Dummy Title 3",
            zoover_review_id=3000003,
            score_aspects=schemas.ScoreAspects().model_dump_json(),
        ),
        schemas.Review(
            id="774673fd-d3f8-471c-a914-66c2afc83e01",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2018-10-03T00:00:00.000Z",
            general_score=9.0,
            text="Dummy text 4",
            title="Dummy Title 4",
            zoover_review_id=4000004,
            score_aspects=schemas.ScoreAspects().model_dump_json(),
        ),
        schemas.Review(
            id="f3fce35a-af4f-40c1-9bda-ce0add8cc888",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2019-09-25T00:00:00.000Z",
            general_score=8.0,
            text="Dummy text 5",
            title="Dummy Title 5",
            zoover_review_id=5000005,
            score_aspects=schemas.ScoreAspects().model_dump_json(),
        ),
        schemas.Review(
            id="3f43180b-9834-46e7-aa8b-6ee56242289b",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2020-06-26T00:00:00.000Z",
            general_score=7.0,
            text="Dummy text 6",
            title="Dummy Title 6",
            zoover_review_id=6000006,
            score_aspects=schemas.ScoreAspects().model_dump_json(),
        ),
        schemas.Review(
            id="114e099c-a4ee-4373-93f0-562e062666e2",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2022-11-02T00:00:00.000Z",
            general_score=9.0,
            text="Dummy text 7",
            title="Dummy Title 7",
            zoover_review_id=7000007,
            score_aspects=schemas.ScoreAspects().model_dump_json(),
        ),
        schemas.Review(
            id="f24e821f-6e60-48b0-9101-d32c1e0520ff",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2023-01-06T00:00:00.000Z",
            general_score=9.0,
            text="Dummy text 8",
            title="Dummy Title 8",
            zoover_review_id=8000008,
            score_aspects=schemas.ScoreAspects().model_dump_json(),
        ),
        schemas.Review(
            id="1f5ae0a4-ddf5-4f73-b57f-eee305034564",
            accommodation_id=ACCOMMODATION_1_ID,
            created_at="2023-01-22T00:00:00.000Z",
            general_score=8.0,
            text="Dummy text 9",
            title="Dummy Title 9",
            zoover_review_id=9000009,
            score_aspects=schemas.ScoreAspects().model_dump_json(),
        ),
    ]

    @staticmethod
    def add(session, review: schemas.Review):
        raise NotImplementedError

    @staticmethod
    def list_for_accommodation(
        session, accommodation_id: uuid.UUID
    ) -> list[schemas.Review]:
        if accommodation_id == MockReviewRepository.ACCOMMODATION_1_ID:
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
