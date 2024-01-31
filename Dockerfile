FROM python:3.11-alpine

WORKDIR /app
RUN pip install poetry && poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml /app/
RUN poetry install -n --no-root --only main --no-cache

COPY ./file_uploader ./