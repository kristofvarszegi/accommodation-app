from data_layer.sqlalchemy_data_layer.database import (
    create_session as create_sqlalchemy_session,
)
from data_layer.sqlalchemy_data_layer.repositories import (
    get_accommodation_repository as get_sqlalchemy_accommodation_repository,
)
from data_layer.sqlalchemy_data_layer.repositories import (
    get_review_repository as get_sqlalchemy_review_repository,
)

# Data backend selectors
create_session = create_sqlalchemy_session
get_accommodation_repository = get_sqlalchemy_accommodation_repository
get_review_repository = get_sqlalchemy_review_repository
