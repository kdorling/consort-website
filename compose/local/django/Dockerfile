# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.11.3-slim-buster

# Add user that will be used in the container.
RUN useradd wagtail

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages required by Wagtail and Django.
# RUN --mount=target=/var/lib/apt/lists,type=cache,sharing=locked \
#     --mount=target=/var/cache/apt,type=cache,sharing=locked \
#     rm -f /etc/apt/apt.conf.d/docker-clean \
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    procps \
    telnet \ 
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Install the project requirements.
COPY ./dev.txt /dev.txt
COPY ./requirements.txt /requirements.txt
RUN pip install -r /dev.txt

# Copy the entrypoint script and make it executable.
COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# Copy the start script for the Django server and make it executable.
COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Copy the start script for the Celery worker and make it executable.
COPY ./compose/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

# Copy the start script for Celery beat and make it executable.
COPY ./compose/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

# Copy the start script for Flower and make it executable.
COPY ./compose/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Set this directory to be owned by the "wagtail" user. This Wagtail project
# uses SQLite, the folder needs to be owned by the user that
# will be writing to the database file.
RUN chown wagtail:wagtail /app

# Copy the source code of the project into the container.
COPY --chown=wagtail:wagtail . .

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# Run the entrypoint script when the container starts.
ENTRYPOINT ["/entrypoint"]
