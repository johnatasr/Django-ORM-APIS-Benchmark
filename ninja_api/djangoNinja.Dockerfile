FROM python:3.8.3-alpine

WORKDIR /user/src/app/

ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYCODE=1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install psycopg2-binary

RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["/user/src/app/entrypoint.sh"]