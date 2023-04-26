FROM python:3.7

WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev

COPY ./posts .

CMD ["flask", "--app", "app.py", "--debug", "run", "--host=0.0.0.0"]
# docker run -p 4000:5000 posts-service == map localhost 4000 to the container's 5000 port
# TODO: use WSGI server like waitress to serve app
