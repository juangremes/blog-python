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

events = []


@app.post('/events')
@check_content_length_of_request_decorator(1000)
def events_post():
    event = request.json
    events.append(event)
    try:
        requests.post(url='http://posts-clusterip-srv:4000/events', json=event)
    except requests.exceptions.ConnectionError:
        app.logger.info('Cannot reach *posts* service')
    try:
        requests.post(url='http://comments-srv:4001/events', json=event)
    except requests.exceptions.ConnectionError:
        app.logger.info('Cannot reach *comments* service')
    try:
        requests.post(url='http://query-srv:4002/events', json=event)
    except requests.exceptions.ConnectionError:
        app.logger.info('Cannot reach *query* service')
    try:
        requests.post(url='http://moderation-srv:4003/events', json=event)
    except requests.exceptions.ConnectionError:
        app.logger.info('Cannot reach *moderation* service')

    return {'status': 'OK'}, 200


@app.get('/events')
def events_get():
    return events, 200

