import json
from typing import Type

import click
from dotenv import load_dotenv
from pydantic import BaseModel

from data_layer.models import Accommodation, Review
from data_layer.sqlalchemy_repository.repositories import (
    SqlAlchemyAccommodationRepository,
    SqlAlchemyReviewRepository,
)
from data_layer.sqlalchemy_repository.session_factory import create_session_factory

OBJECT_TYPE_TO_CLASS = {"accommodations": Accommodation, "reviews": Review}
OBJECT_TYPE_TO_REPOSITORY_CLASS = {
    "accommodations": SqlAlchemyAccommodationRepository,
    "reviews": SqlAlchemyReviewRepository,
}

load_dotenv()


def load_objects(objects_file: click.File, klass: Type[BaseModel]) -> list[BaseModel]:
    objects = json.load(objects_file)
    objects = [klass(**object) for object in objects]
    return objects


@click.command()
@click.argument(
    "object_type",
    type=click.Choice(["accommodations", "reviews"], case_sensitive=False),
    required=True,
)
@click.argument("objects_file", type=click.File("r"), required=True)
def import_data(object_type: str, objects_file: click.File):
    objects = load_objects(objects_file, OBJECT_TYPE_TO_CLASS[object_type])
    session_factory = create_session_factory()
    with session_factory() as session:
        object_repository = OBJECT_TYPE_TO_REPOSITORY_CLASS[object_type](session)
        for object in objects:
            object_repository.add(object)
        session.commit()


if __name__ == "__main__":
    import_data()
