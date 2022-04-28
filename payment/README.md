# Payment Service

## Getting Started

Start containers:
```shell
docker-compose up --build
```

API docs (Swagger UI) are reached via http://localhost:8080/docs/

## Develop
Activate virtual environment
```shell
poetry shell
```

Install dependencies
```shell
poetry install --remove-untracked
```

Run tests
```shell
pytest tests
```
