from freezegun import freeze_time

from scoring.accommodation_scores import calculate_accommodation_scores
from tests.conftest import MockReviewRepository


@freeze_time("2023-04-01")
def test_get_accommodation_ratings():
    ratings = calculate_accommodation_scores(
        MockReviewRepository.list_for_accommodation(
            None, MockReviewRepository.ACCOMMODATION_1_ID
        )
    )
    assert ratings.general_score == 8.63
    for score_aspect_name in ratings.score_aspects.model_fields:
        assert getattr(ratings.score_aspects, score_aspect_name) == 0


@freeze_time("2100-01-01")
def test_get_accommodation_ratings_when_all_reviews_are_old():
    ratings = calculate_accommodation_scores(
        MockReviewRepository.list_for_accommodation(
            None, MockReviewRepository.ACCOMMODATION_1_ID
        )
    )
    assert ratings.general_score == 8.33
    for score_aspect_name in ratings.score_aspects.model_fields:
        assert getattr(ratings.score_aspects, score_aspect_name) == 0


# TODO
# def test_get_accommodation_ratings_when_no_reviews_are_old():
