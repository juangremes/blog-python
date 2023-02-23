from flask import Flask, request, abort
from flask_cors import CORS
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
CORS(app)


@app.post('/events')
@check_content_length_of_request_decorator(1000)
def post_events():
    event = request.get_data()
    requests.post(url='http://localhost:4000/events', data=event)
    requests.post(url='http://localhost:4001/events', data=event)
    requests.post(url='http://localhost:4002/events', data=event)
    return {'status': 'OK'}, 200

