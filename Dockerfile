FROM python:3.12-alpine3.20

LABEL maintainer="operations-engineering <operations-engineering@digital.justice.gov.uk>"

# Install system dependencies
RUN apk add --no-cache --no-progress \
  libffi-dev \
  build-base \
  curl \
  && apk update \
  && apk upgrade --no-cache --available

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip==24.2 pipenv==2024.1.0

# Create user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup -u 1051

# Set working directory
WORKDIR /home/operations-engineering-application

# Change ownership of the working directory
RUN chown -R appuser:appgroup /home/operations-engineering-application

# Switch to non-root user
USER appuser

# Copy Pipfile and Pipfile.lock
COPY --chown=appuser:appgroup Pipfile Pipfile.lock ./

# Install dependencies without --system
RUN pipenv install --deploy --ignore-pipfile

# Copy application code
COPY --chown=appuser:appgroup app app

# Copy data file 
COPY --chown=appuser:appgroup data/main_acronyms_df_rated_cleaned.csv .

# Copy the entrypoint script
COPY --chown=appuser:appgroup entrypoint.sh .

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh


# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

USER 1051

# Expose port
EXPOSE 4567

# Healthcheck
HEALTHCHECK --interval=60s --timeout=30s CMD curl -I -XGET http://localhost:4567 || exit 1

# Use pipenv to run gunicorn
ENTRYPOINT ["/home/operations-engineering-application/entrypoint.sh"]
