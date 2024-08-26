# Accommodation App

## Introduction

TODO

data_layer.config

## Implementation status

| Component        | Feature/Task                             | Status                  |
| ---------------- | ---------------------------------------- | ----------------------- |
| Data import tool | Supports importing accommodations        | TODO Tests              |
| Data import tool | Supports importing reviews               | TODO Tests              |
| Data service     | List all accommodations                  | Done                    |
| Data service     | Get a single accommodation               | Done                    |
| Data service     | List all reviews for an accommodation    | Done                    |
| Data service     | Get a single review for an accommodation | Done                    |
| Scoring service  | Get rating                               | TODO Tests              |
| Scoring service  | Optimize score calculation               | TODO                    |
| General          | Containerize/Deploy                      | TODO                    |
| General          | Documentation                            | TODO                    |

## A few possible future improvements e.g on the way to production

- Create mock DB for testing
- Maximal test coverage in terms of e.g. execution paths, partitions
- Automated end-to-end tests
- Cache frequently requested accommodations and ratings
- Splitting requirements.txt for data_importer, data_service, scoring_service, dev
- API endpoint versioning
- API documentation (using e.g. Swagger)
- GitHub Actions: Test; Build and deploy to the cloud
- Define SQLAlchemy models via mapping from their corresponding Pydantic models

## Quickstart

TODO

Ubuntu 24.04 on WSL 2

https://docs.docker.com/engine/install/ubuntu/

```bash
docker run -d --name accommodation-app-postgres -e POSTGRES_PASSWORD=12345678 -p 5432:5432 postgres
```

```bash
docker exec -it accommodation-app-postgres psql -h db -U postgres -p 5432
docker exec -it accommodation-app-db-1 psql -h db -U dev -p 5432 -d accommodation_app
```

```sql
CREATE DATABASE <DB name>;
CREATE USER <DB username> WITH PASSWORD '<DB password>';
ALTER DATABASE <DB name> OWNER TO <DB username>;
```

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

.env file:

```
DB_USERNAME=<DB username>
DB_PASSWORD=<DB password>
DB_HOST=<DB host>
DB_NAME=<DB name>
```

```bash
export PYTHONPATH=$PWD
```

```bash
python data_importer/import_data.py accommodations ../Backend\ Tech\ Assignment/accommodations.json
python data_importer/import_data.py reviews ../Backend\ Tech\ Assignment/reviews.json
```

```sql
SELECT * FROM accommodations;
SELECT * FROM reviews;
```

```bash
fastapi run data_service_fastapi/main.py
```

```bash
fastapi run scoring_service_fastapi/main.py
```

```bash
docker build -t data-service-fastapi -f Dockerfile.data_service_fastapi .
docker build -t scoring-service-fastapi -f Dockerfile.scoring_service_fastapi .
```

```bash
docker run -d --name data-service-fastapi -p 80:80 data-service-fastapi
docker run -d --name scoring-service-fastapi -p 80:80 scoring-service-fastapi
```

```bash
curl http://localhost:8000/accommodations/
```

```bash
curl http://localhost:8000/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/
```

```bash
curl http://localhost:8000/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/reviews/
```

```bash
curl http://localhost:8000/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/reviews/4aa80891-ed4e-4419-9d17-c3a2965d53b6
```

## Sources

[Cosmic Python](https://www.cosmicpython.com/)

[FastAPI - SQL (Relational) Databases and other official docs](https://fastapi.tiangolo.com/tutorial/sql-databases/)

[Setting up a FastAPI App with Async SQLALchemy 2.0 & Pydantic V2](https://medium.com/@tclaitken/setting-up-a-fastapi-app-with-async-sqlalchemy-2-0-pydantic-v2-e6c540be4308)
