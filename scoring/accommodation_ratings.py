import math  # TODO Is numpy faster?
from datetime import date, datetime

from data_layer import schemas

SCORE_ROUNDING_NDIGITS = 2

# Pre-compute ln values so only a lookup is needed when calculating ratings
X_TO_LN_X = {x: math.log(x) for x in range(1, 25)}
OLD_REVIEWS_WEIGHT = math.log(1.77)


# TODO Tests
def datetime_to_floored_months(datetime_: datetime) -> int:
    return datetime_.year * 12 + datetime_.month


# TODO Tests
def calculate_age_in_months(
    current_date_in_floored_months: int, review_datetime: datetime
) -> int:
    return current_date_in_floored_months - datetime_to_floored_months(review_datetime)


# TODO Tests
def calculate_review_weight(review_age_in_months: int) -> float:
    return X_TO_LN_X[25 - review_age_in_months]


# TODO Tests
def calculate_accommodation_ratings(
    reviews: list[schemas.Review],
) -> schemas.AccommodationRatings:
    if len(reviews) == 0:
        raise ValueError("Cannot calculate rating with zero number of reviews")

    # Create age[month] array
    # score_weights = np.array((len(reviews),))
    general_score_weighted_sum = 0.0
    sum_of_weights = 0.0
    old_review_general_scores = []
    current_date_in_floored_months = datetime_to_floored_months(datetime.now())

    # TODO Sub-scores; optimize
    for review in reviews:
        review_age_in_months = calculate_age_in_months(
            current_date_in_floored_months, review.created_at
        )
        if review_age_in_months < 24:
            review_weight = calculate_review_weight(review_age_in_months)
            general_score_weighted_sum += review_weight * review.general_score
            sum_of_weights += review_weight
        else:
            old_review_general_scores.append(review.general_score)

    if old_review_general_scores:
        old_reviews_general_score_weighted_sum = (
            OLD_REVIEWS_WEIGHT
            * sum(old_review_general_scores)
            / len(old_review_general_scores)
        )
        general_score_weighted_sum += old_reviews_general_score_weighted_sum
        sum_of_weights += OLD_REVIEWS_WEIGHT

    general_score_weighted_avg = round(
        general_score_weighted_sum / sum_of_weights, SCORE_ROUNDING_NDIGITS
    )

    return schemas.AccommodationRatings(general_score=general_score_weighted_avg)
