FROM python:3.10-slim-bullseye

ARG APP_ENV=production

ENV PYTHONPATH=/code/src
ENV APP_ENV=$APP_ENV

RUN addgroup landbot && useradd -u 1000 landbot -g landbot -G tty

RUN set -ex && \
  apt-get update --yes && \
  apt-get upgrade --yes && \
  apt-get install --no-install-recommends --yes curl build-essential libpq-dev gettext dnsutils procps strace libc-bin libexpat1 libcurl4-openssl-dev git libpcre3 libpcre3-dev libssl-dev sqlite3 libsqlite3-dev && \
    pip install --no-cache-dir --disable-pip-version-check pip-tools

COPY --chown=landbot:landbot ./requirements /tmp/requirements
RUN pip install -r /tmp/requirements/base.txt

RUN if ! [ $APP_ENV = 'production' ]; \
    then \
    pip-sync /tmp/requirements/base.txt /tmp/requirements/test.txt /tmp/requirements/linting.txt --pip-args '--no-cache-dir --no-deps --disable-pip-version-check'; \
    fi

RUN mkdir -m 775 /code && \
    chown landbot:landbot /code
COPY --chown=landbot:landbot . /code/
WORKDIR /code

USER landbot

EXPOSE 8001

CMD gunicorn -c ./landbot_challenge/gunicorn_conf.py landbot_challenge.wsgi.py
