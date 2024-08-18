# Accommodation App

## Introduction

TODO

data_layer.config

## Implementation status

| Component        | Feature/Task                             | Status                 | Priority     |
| ---------------- | ---------------------------------------- | ---------------------- | ------------ |
| Data import tool | Supports importing accommodations        | TODO tests             | Must         |
| Data import tool | Supports importing reviews               | TODO sub-scores, tests | Must         |
| Data service     | List all accommodations                  | Done                   | Must         |
| Data service     | Get a single accommodation               | Done                   | Must         |
| Data service     | List all reviews for an accommodation    | Done                   | Must         |
| Data service     | Get a single review for an accommodation | Done                   | Must         |
| Scoring service  | TODO                                     | TODO                   | Must         |
| Scoring service  | Optimize score calculation               | TODO                   | Nice to have |
| General          | Containerize/Deploy                      | TODO                   | Nice to have |

## A few possible future improvements e.g on the way to production

- Create mock DB for testing
- Maximal test coverage in various terms e.g. execution paths, partitions
- Automated end-to-end tests
- Splitting requirements.txt for data_importer, data_service, scoring_service, dev
- API endpoint versioning
- API documentation (using e.g. Swagger)
- GitHub Actions: Test; Build and deploy to the cloud

## Quickstart

TODO

```json
python data_importer/import_data.py accommodations ../Backend\ Tech\ Assignment/accommodations.json
```

```json
python data_importer/import_data.py reviews ../Backend\ Tech\ Assignment/reviews.json
```

curl http://localhost:8000/accommodations/

curl http://localhost:8000/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/

curl http://localhost:8000/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/reviews/

curl http://localhost:8000/accommodations/dddaebf8-2e22-4699-8db0-f10fad2f2f8f/one-review/

## Creating development environment

TODO

venv

requirements_dev.txt

postgres DB, user - with docker-compose/extended image

.env

## Sources

[Cosmic Python](https://www.cosmicpython.com/)

[FastAPI - SQL (Relational) Databases and other official docs](https://fastapi.tiangolo.com/tutorial/sql-databases/)

[Setting up a FastAPI App with Async SQLALchemy 2.0 & Pydantic V2](https://medium.com/@tclaitken/setting-up-a-fastapi-app-with-async-sqlalchemy-2-0-pydantic-v2-e6c540be4308)
