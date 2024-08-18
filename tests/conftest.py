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
    @staticmethod
    def add(session, review: schemas.Review):
        raise NotImplementedError

    @staticmethod
    def get_for_accommodation(
        session, accommodation_id: uuid.UUID
    ) -> list[schemas.Review]:
        if accommodation_id == uuid.UUID("c9b7158b-1b07-4941-82d1-9ef8221e649d"):
            return [
                schemas.Review(
                    id="2cf4abc9-7b7c-4876-8d85-965eebeca34d",
                    general_score=3.14,
                    accommodation_id="c9b7158b-1b07-4941-82d1-9ef8221e649d",
                ),
                schemas.Review(
                    id="6f102399-70dd-4302-be62-8186bd3149f0",
                    general_score=3.15,
                    accommodation_id="c9b7158b-1b07-4941-82d1-9ef8221e649d",
                ),
            ]
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="No reviews found for accommodation",
            )

    @staticmethod
    def get_one_review_for_accommodation(
        session, accommodation_id: uuid.UUID
    ) -> schemas.Review:
        if accommodation_id == uuid.UUID("c9b7158b-1b07-4941-82d1-9ef8221e649d"):
            return schemas.Review(
                id="6f102399-70dd-4302-be62-8186bd3149f0",
                general_score=3.15,
                accommodation_id="c9b7158b-1b07-4941-82d1-9ef8221e649d",
            )
        else:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="No reviews found for accommodation",
            )
