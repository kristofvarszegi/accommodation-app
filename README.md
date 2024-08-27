# Accommodation App

## Implementation highlights

- Employs the repository pattern for separating the data layer from the business logic. The concrete repository implementation to be used is selected in data_layer/config.py.
- The service layer is separated from the data layer
- The services use FastAPI and share the schemas with the repositories. The schemas essentially model the domain.
- Containerized (see docker-compose.yml and the Quickstart section below)

## Quickstart

Tested on Ubuntu 24.04 on WSL 2, with Python 3.12.3, and with Docker installed following [this guide](https://docs.docker.com/engine/install/ubuntu/).

Run the following commands in an elevated shell:

1. Launch the database:

   ```bash
   docker compose up -d db
   ```

2. Create a Python environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Apply the DB migrations:

   ```bash
   alembic upgrade head
   ```

4. Import the data to the DB. (The credentials are stored in .env for demonstration purposes.) Insert the path to the accommodations and the reviews file in the corresponding commands.

   ```bash
   export PYTHONPATH=$PWD
   python data_importer/import_data.py accommodations <path to accommodations.json>
   python data_importer/import_data.py reviews <path to reviews.json>
   ```

   For example:

   ```bash
   export PYTHONPATH=$PWD
   python data_importer/import_data.py accommodations ../Backend\ Tech\ Assignment/accommodations.json
   python data_importer/import_data.py reviews ../Backend\ Tech\ Assignment/reviews.json
   ```

5. Deactivate the development environment just to see that the services are really independent from the local Python environment:

   ```bash
   deactivate
   ```

6. Run the services

   ```bash
   docker compose up -d data_service_fastapi scoring_service_fastapi
   ```

7. Try the Data Service using the following commands:

   ```bash
   curl http://localhost:80/accommodations/

   curl http://localhost:80/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/

   curl http://localhost:80/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/reviews/

   curl http://localhost:80/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/reviews/4aa80891-ed4e-4419-9d17-c3a2965d53b6
   ```

8. Try the Scoring Service using the following command:

   ```bash
   curl http://localhost:81/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/scores/
   ```

## A few possible future improvements e.g on the way to production

- Performance-optimize the score service by tracking the weighted score sums and the weight sums in e.g. a table
- Create mock DB for testing
- Maximal test coverage in terms of e.g. execution paths, partitions
- Automated end-to-end tests
- Cache frequently requested accommodations and ratings
- Splitting requirements.txt for data_importer, data_service, scoring_service, dev
- API endpoint versioning
- API documentation (using e.g. Swagger)
- GitHub Actions: Test; Build and deploy to the cloud
- Define SQLAlchemy models via mapping from their corresponding Pydantic models

## Sources

[Cosmic Python](https://www.cosmicpython.com/)

[FastAPI - SQL (Relational) Databases and other official docs](https://fastapi.tiangolo.com/tutorial/sql-databases/)

[Setting up a FastAPI App with Async SQLALchemy 2.0 & Pydantic V2](https://medium.com/@tclaitken/setting-up-a-fastapi-app-with-async-sqlalchemy-2-0-pydantic-v2-e6c540be4308)
