import json
from typing import Type

import click
from pydantic import BaseModel

from data_layer.schemas import Accommodation, Review
from data_layer.sqlalchemy_data_layer.database import session_factory
from data_layer.sqlalchemy_data_layer.repositories import (
    SqlAlchemyAccommodationRepository,
    SqlAlchemyReviewRepository,
)

ITEM_TYPE_TO_CLASS = {"accommodations": Accommodation, "reviews": Review}
ITEM_TYPE_TO_REPOSITORY_CLASS = {
    "accommodations": SqlAlchemyAccommodationRepository,
    "reviews": SqlAlchemyReviewRepository,
}


def load_items(items_file: click.File, klass: Type[BaseModel]) -> list[BaseModel]:
    items = json.load(items_file)
    items = [klass(**item) for item in items]
    return items


@click.command()
@click.argument(
    "item_type",
    type=click.Choice(["accommodations", "reviews"], case_sensitive=False),
    required=True,
)
@click.argument("items_file", type=click.File("r", encoding="utf-8"), required=True)
def import_data(item_type: str, items_file: click.File):
    items = load_items(items_file, ITEM_TYPE_TO_CLASS[item_type])
    with session_factory() as session:
        item_repository = ITEM_TYPE_TO_REPOSITORY_CLASS[item_type]
        for item in items:
            item_repository.add(session, item)
        session.commit()


if __name__ == "__main__":
    import_data()
