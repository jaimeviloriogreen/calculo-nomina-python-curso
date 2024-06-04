FROM python:3.12-slim

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --ignore-pipfile

COPY src/ src/

CMD ["pipenv", "run", "start"]