FROM python:3.7

WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev

COPY ./event-bus .

CMD ["flask", "run", "--host=0.0.0.0"]
# docker run -p 4005:5000 posts-service
# TODO: use WSGI server like waitress to serve app
