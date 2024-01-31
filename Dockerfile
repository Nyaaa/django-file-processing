FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
RUN pip install poetry && poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml /app/
RUN poetry install -n --no-root --only main --no-cache

COPY ./file_uploader ./