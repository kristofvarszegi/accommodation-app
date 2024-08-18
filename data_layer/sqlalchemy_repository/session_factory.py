import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session_factory() -> sessionmaker:
    db_username = os.environ["DB_USERNAME"]
    db_password = os.environ["DB_PASSWORD"]
    db_host = os.environ["DB_HOST"]
    db_name = os.environ["DB_NAME"]
    engine = create_engine(
        f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}/{db_name}"
    )
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
