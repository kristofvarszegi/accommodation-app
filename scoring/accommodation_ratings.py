import math
from datetime import date
from functools import partial
from typing import Optional

import pandas as pd

from data_layer import schemas

SCORE_ROUNDING_NDIGITS = 2

# Pre-compute weight values so only a lookup is needed when calculating scores
AGE_MONTHS_TO_WEIGHT = {
    age_months: math.log(25 - age_months) for age_months in range(0, 23)
}
OLD_REVIEWS_WEIGHT = math.log(1.77)

DATE_LABEL = "date"
GENERAL_SCORE_LABEL = "general_score"
WEIGHT_LABEL = "weight"

SCORE_COL_LABELS = [GENERAL_SCORE_LABEL, *schemas.ScoreAspects.model_fields.keys()]


# TODO Tests
def calculate_individual_weight(
    current_date: date, review_date: date
) -> Optional[float]:
    review_age_months = (
        current_date.year * 12
        + current_date.month
        - (review_date.year * 12 + review_date.month)
    )
    return AGE_MONTHS_TO_WEIGHT[review_age_months] if review_age_months < 24 else None


# TODO Clearer names for "...individual..."
# TODO Tests
def calculate_accommodation_scores(
    reviews: list[schemas.Review],
) -> schemas.AccommodationScores:
    if len(reviews) == 0:
        raise ValueError("Cannot calculate rating with zero number of reviews")

    scores = [
        {
            DATE_LABEL: review.created_at.date(),
            GENERAL_SCORE_LABEL: review.general_score,
            **review.score_aspects.model_dump(),
        }
        for review in reviews
    ]
    scores = pd.DataFrame(scores, columns=[DATE_LABEL, *SCORE_COL_LABELS])

    scores[WEIGHT_LABEL] = scores[DATE_LABEL].apply(
        partial(calculate_individual_weight, date.today())
    )
    scores.drop(DATE_LABEL, axis=1, inplace=True)
    weight_isna = scores[WEIGHT_LABEL].isna()

    scores.loc[~weight_isna, SCORE_COL_LABELS] = scores[~weight_isna][
        SCORE_COL_LABELS
    ].multiply(scores[~weight_isna][WEIGHT_LABEL], axis="index")
    weights_sum = scores[WEIGHT_LABEL].sum()
    individual_score_weighted_sums = scores[~weight_isna].sum()

    if weight_isna.sum() > 0:
        weights_sum += OLD_REVIEWS_WEIGHT
        old_score_averages_times_weight = (
            scores[weight_isna].mean().multiply(OLD_REVIEWS_WEIGHT)
        )

    weighted_averages = (
        (
            individual_score_weighted_sums.add(old_score_averages_times_weight)
            / weights_sum
        )
        .astype(float)
        .round(SCORE_ROUNDING_NDIGITS)
    )
    weighted_averages.fillna(0.0, inplace=True)

    return schemas.AccommodationScores(
        general_score=weighted_averages[GENERAL_SCORE_LABEL],
        score_aspects=schemas.ScoreAspects(
            **weighted_averages[list(schemas.ScoreAspects.model_fields.keys())]
        ),
    )
