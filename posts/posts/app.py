import uuid

from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

posts = {}

print('v56')


@app.get('/posts')  # this is not used
def posts_get():
    return posts, 200


@app.post('/posts')
def posts_post():
    data = request.json
    id: str = uuid.uuid1().hex
    title: str = data.get('title')
    posts[id] = {'id': id, 'title': title}
    requests.post(url='http://event-bus-srv:4005/events', json={  # this is synchronous
        'type': 'PostCreated',
        'data': {
            'id': id,
            'title': title
        }
    })
    return posts[id], 201


@app.post('/events')
def posts_receive_events_post():
    print(f"Received Event: {request.json.get('type')}")
    return {}, 200
