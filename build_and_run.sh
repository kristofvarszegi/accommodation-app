# Create development environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the DB
docker compose up -d db

# Apply DB migrations
alembic upgrade head

# Import the data to the DB. Credentials are stored in .env for demonstration purposes.
export PYTHONPATH=$PWD
python data_importer/import_data.py accommodations ../Backend\ Tech\ Assignment/accommodations.json
python data_importer/import_data.py reviews ../Backend\ Tech\ Assignment/reviews.json

# Deactivate the development environment to see that the services are really containerized
deactivate

# Run the services
docker compose up -d data_service_fastapi scoring_service_fastapi
