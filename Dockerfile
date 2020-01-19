FROM python:3.7-alpine
MAINTAINER Anton Maistrenko

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN apk add gettext

RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
RUN mkdir /app/material

WORKDIR /app
COPY ./app /app
COPY ./filefield_cache /app/filefield_cache
COPY ./docker /app/docker

RUN chmod +x /app/docker/start.sh

CMD ["sh", "/app/docker/start.sh"]