#!/bin/sh

# Navigate to the application directory
cd /home/operations-engineering-application

# Ensure all environment variables are set
export FLASK_APP="app.run:app()"  # Set this to your Flask app

# Run database migrations
echo "Applying database migrations..."
pipenv run flask db upgrade --directory "app/migrations"


# Start Gunicorn with the specified app
pipenv run gunicorn --bind=0.0.0.0:4567 "app.run:app()"

