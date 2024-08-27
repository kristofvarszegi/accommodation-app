from datetime import date
from typing import Optional

import pytest
from freezegun import freeze_time

from scoring.scoring import calculate_accommodation_scores, calculate_individual_weight
from tests.conftest import MockReviewRepository


@pytest.mark.parametrize(
    "current_date,review_date,expected_individual_weight",
    (
        (date(2024, 8, 27), date(2024, 8, 1), 3.2188758248682006),
        (date(2024, 8, 27), date(2024, 7, 1), 3.1780538303479458),
        (date(2024, 8, 27), date(2024, 6, 1), 3.1354942159291497),
        (date(2024, 8, 27), date(2024, 5, 1), 3.091042453358316),
        (date(2024, 8, 27), date(2024, 4, 1), 3.044522437723423),
        (date(2024, 8, 27), date(2024, 3, 1), 2.995732273553991),
        (date(2024, 8, 27), date(2024, 2, 1), 2.9444389791664403),
        (date(2024, 8, 27), date(2024, 1, 1), 2.8903717578961645),
        (date(2024, 8, 27), date(2023, 12, 1), 2.833213344056216),
        (date(2024, 8, 27), date(2023, 11, 1), 2.772588722239781),
        (date(2024, 8, 27), date(2023, 10, 1), 2.70805020110221),
        (date(2024, 8, 27), date(2023, 9, 1), 2.6390573296152584),
        (date(2024, 8, 27), date(2023, 8, 1), 2.5649493574615367),
        (date(2024, 8, 27), date(2023, 7, 1), 2.4849066497880004),
        (date(2024, 8, 27), date(2023, 6, 1), 2.3978952727983707),
        (date(2024, 8, 27), date(2023, 5, 1), 2.302585092994046),
        (date(2024, 8, 27), date(2023, 4, 1), 2.1972245773362196),
        (date(2024, 8, 27), date(2023, 3, 1), 2.0794415416798357),
        (date(2024, 8, 27), date(2023, 2, 1), 1.9459101490553132),
        (date(2024, 8, 27), date(2023, 1, 1), 1.791759469228055),
        (date(2024, 8, 27), date(2022, 12, 1), 1.6094379124341003),
        (date(2024, 8, 27), date(2022, 11, 1), 1.3862943611198906),
        (date(2024, 8, 27), date(2022, 10, 1), 1.0986122886681098),
        (date(2024, 8, 27), date(2022, 9, 1), 0.6931471805599453),
        (date(2024, 8, 27), date(2022, 8, 1), None),
        (date(2024, 8, 27), date(2022, 7, 1), None),
    ),
)
def test_calculate_individual_weight(
    current_date: date, review_date: date, expected_individual_weight: Optional[float]
):
    individual_weight = calculate_individual_weight(current_date, review_date)
    assert individual_weight == expected_individual_weight


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
