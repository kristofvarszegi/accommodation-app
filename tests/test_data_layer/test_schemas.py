import json

from data_layer import schemas


def test_deserialize_review():
    # Arrange
    serialized_review = {
        "id": "6f102399-70dd-4302-be62-8186bd3149f0",
        "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
        "createdAt": "2018-05-26T00:00:00.000Z",
        "generalScore": 8.0,
        "text": "Dummy text 2",
        "title": "Dummy Title 2",
        "zooverReviewId": 2000002,
        "scoreAspects": json.dumps(
            {
                "childFriendly": 1.2,
                "food": 2.3,
                "hygiene": 3.4,
                "location": 4.5,
                "pool": 5.6,
                "priceQuality": 6.7,
                "room": 7.8,
                "service": 8.9,
            }
        ),
    }
    expected_deserialized_review = schemas.Review(
        id="6f102399-70dd-4302-be62-8186bd3149f0",
        accommodation_id="c9b7158b-1b07-4941-82d1-9ef8221e649d",
        created_at="2018-05-26T00:00:00.000Z",
        general_score=8.0,
        text="Dummy text 2",
        title="Dummy Title 2",
        zoover_review_id=2000002,
        score_aspects=schemas.ScoreAspects(
            child_friendly=1.2,
            food=2.3,
            hygiene=3.4,
            location=4.5,
            pool=5.6,
            price_quality=6.7,
            room=7.8,
            service=8.9,
        ).model_dump_json(),
    )

    # Act
    deserialized_review = schemas.Review(**serialized_review)

    # Assert
    assert deserialized_review == expected_deserialized_review


def test_serialize_review():
    # Arrange
    deserialized_review = schemas.Review(
        id="6f102399-70dd-4302-be62-8186bd3149f0",
        accommodation_id="c9b7158b-1b07-4941-82d1-9ef8221e649d",
        created_at="2018-05-26T00:00:00.000Z",
        general_score=8.0,
        text="Dummy text 2",
        title="Dummy Title 2",
        zoover_review_id=2000002,
        score_aspects=schemas.ScoreAspects(
            child_friendly=1.2,
            food=None,
            hygiene=3.4,
            location=None,
            pool=5.6,
            price_quality=None,
            room=7.8,
            service=None,
        ).model_dump_json(),
    )
    expected_serialized_review = json.dumps(
        {
            "id": "6f102399-70dd-4302-be62-8186bd3149f0",
            "accommodationId": "c9b7158b-1b07-4941-82d1-9ef8221e649d",
            "createdAt": "2018-05-26T00:00:00.000000+00:00",
            "generalScore": 8.0,
            "text": "Dummy text 2",
            "title": "Dummy Title 2",
            "zooverReviewId": 2000002,
            "scoreAspects": json.dumps(
                {"childFriendly": 1.2, "hygiene": 3.4, "pool": 5.6, "room": 7.8},
                separators=(",", ":"),
            ),
        },
        separators=(",", ":"),
    )

    # Act
    serialized_review = deserialized_review.model_dump_json(by_alias=True)

    # Assert
    assert serialized_review == expected_serialized_review
