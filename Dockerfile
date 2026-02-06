FROM python:3.13.7-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.loc ./

RUN poetry install --no--root

COPY . .

CMD ["poetry", "run", "uvicorn", "app.main::app", "--host", "0.0.0.0", "--port", "8000"]
