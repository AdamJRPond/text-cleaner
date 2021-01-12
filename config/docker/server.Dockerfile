FROM python:3.7

WORKDIR /app

COPY Pipfile  /app/

RUN pip install pipenv 

RUN pipenv install

RUN pipenv run python -m nltk.downloader popular

COPY main.py utils.py /app/

