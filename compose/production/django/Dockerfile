FROM python:3.11.3-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    netcat \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    python-dev \
    libxml2-dev \
    libxslt1-dev \
    antiword \
    unrtf \
    poppler-utils \
    tesseract-ocr \
    flac \
    ffmpeg \
    lame \
    libmad0 \
    libsox-fmt-mp3 \
    sox \
    libjpeg-dev \
    swig \
    libpulse-dev \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN addgroup --system wagtail \
    && adduser --system --ingroup wagtail wagtail

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint
RUN chown wagtail /entrypoint

COPY ./compose/production/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
RUN chown wagtail /start

COPY ./compose/production/django/celery/worker/start-highpriority /start-celeryworker-highpriority
RUN sed -i 's/\r$//g' /start-celeryworker-highpriority
RUN chmod +x /start-celeryworker-highpriority
RUN chown wagtail /start-celeryworker-highpriority

COPY ./compose/production/django/celery/worker/start-lowpriority /start-celeryworker-lowpriority
RUN sed -i 's/\r$//g' /start-celeryworker-lowpriority
RUN chmod +x /start-celeryworker-lowpriority
RUN chown wagtail /start-celeryworker-lowpriority

COPY ./compose/production/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat
RUN chown wagtail /start-celerybeat

COPY ./compose/production/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

# COPY ./compose/production/django/celery/supervisord.conf /supervisord.conf
# RUN sed -i 's/\r$//g' /supervisord.conf

RUN mkdir /var/run/celery
RUN mkdir /var/log/celery
RUN chown wagtail:wagtail /var/run/celery
RUN chown wagtail:wagtail /var/log/celery

RUN mkdir /app
RUN mkdir /app/staticfiles
RUN mkdir /app/mediafiles
WORKDIR /app

# copy project code
COPY ./app .

RUN chown -R wagtail:wagtail /app

USER wagtail

ENTRYPOINT ["/entrypoint"]