FROM python:3.11-slim

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install --upgrade pip

#COPY Pipfile Pipfile.lock /solutionfactory-test-task/
RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --system

ENV MONGODB_HOST="mongodb"
ENV MONGODB_PORT="27017"

COPY . .
#WORKDIR /completed-forms
