from flask import Flask, request
import requests

app = Flask(__name__)


@app.post('/events')
def moderation_events_post():
    payload = request.json
    event_type = payload.get('type')
    data = payload.get('data')

    if event_type == 'CommentCreated':
        status = 'rejected' if 'orange' in data.get('content') else 'approved'
        requests.post(url='http://localhost:4005/events', json={
            'type': 'CommentModerated',
            'data': {
                'id': data.get('id'),
                'postId': data.get('postId'),
                'status': status,
                'content': data.get('content')
            }

        })

    return {}, 200
