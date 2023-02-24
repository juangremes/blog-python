from flask import Flask, request, abort
import functools
import requests


def check_content_length_of_request_decorator(max_content_length):
    def wrapper(fn):
        @functools.wraps(fn)
        def decorated_view(*args, **kwargs):
            if int(request.headers.get('Content-Length') or 0) > max_content_length:
                return abort(400, description='Too much content in request')
            else:
                return fn(*args, **kwargs)
        return decorated_view
    return wrapper


app = Flask(__name__)


@app.post('/events')
@check_content_length_of_request_decorator(1000)
def events_post():
    event = request.json
    requests.post(url='http://localhost:4000/events', json=event)
    requests.post(url='http://localhost:4001/events', json=event)
    requests.post(url='http://localhost:4002/events', json=event)
    requests.post(url='http://localhost:4003/events', json=event)
    return {'status': 'OK'}, 200

