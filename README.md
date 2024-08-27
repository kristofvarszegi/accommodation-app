# Accommodation App

## Introduction

TODO

data_layer.config

## Implementation status

| Component        | Feature/Task                             | Status     |
| ---------------- | ---------------------------------------- | ---------- |
| Data import tool | Supports importing accommodations        | TODO Tests |
| Data import tool | Supports importing reviews               | TODO Tests |
| Data service     | List all accommodations                  | Done       |
| Data service     | Get a single accommodation               | Done       |
| Data service     | List all reviews for an accommodation    | Done       |
| Data service     | Get a single review for an accommodation | Done       |
| Scoring service  | Get rating                               | TODO Tests |
| Scoring service  | Optimize score calculation               | TODO       |
| General          | Containerize/Deploy                      | TODO       |
| General          | Documentation                            | TODO       |

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

You may need to run the following commands in an elevated shell.

```bash
chmod +x build_and_run.sh
./build_and_run.sh
```

```bash
curl http://localhost:80/accommodations/
curl http://localhost:80/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/
curl http://localhost:80/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/reviews/
curl http://localhost:80/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/reviews/4aa80891-ed4e-4419-9d17-c3a2965d53b6
```

```bash
curl http://localhost:81/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/scores/
```

## Sources

[Cosmic Python](https://www.cosmicpython.com/)

[FastAPI - SQL (Relational) Databases and other official docs](https://fastapi.tiangolo.com/tutorial/sql-databases/)

[Setting up a FastAPI App with Async SQLALchemy 2.0 & Pydantic V2](https://medium.com/@tclaitken/setting-up-a-fastapi-app-with-async-sqlalchemy-2-0-pydantic-v2-e6c540be4308)

## Miscellaneous commands

```bash
docker run -d --name accommodation-app-postgres -e POSTGRES_PASSWORD=12345678 -p 5432:5432 postgres
docker exec -it accommodation-app-postgres psql -h db -U postgres -p 5432
docker exec -it accommodation-app-db-1 psql -h db -U dev -p 5432 -d accommodation_app
```

```sql
CREATE DATABASE <DB name>;
CREATE USER <DB username> WITH PASSWORD '<DB password>';
ALTER DATABASE <DB name> OWNER TO <DB username>;
```

```sql
SELECT * FROM accommodations;
SELECT * FROM reviews;
```

```bash
fastapi run data_service_fastapi/main.py
fastapi run scoring_service_fastapi/main.py
```

```bash
docker build -t data-service-fastapi -f Dockerfile.data_service_fastapi .
docker build -t scoring-service-fastapi -f Dockerfile.scoring_service_fastapi .
```

```bash
docker run -d --name data-service-fastapi -p 80:80 data-service-fastapi
docker run -d --name scoring-service-fastapi -p 81:81 scoring-service-fastapi
```
