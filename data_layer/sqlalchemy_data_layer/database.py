import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_username = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]
db_host = os.environ["DB_HOST"]
db_name = os.environ["DB_NAME"]
engine = create_engine(
    f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}/{db_name}"
)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_session():
    session = session_factory()
    try:
        yield session
    finally:
        session.close()
