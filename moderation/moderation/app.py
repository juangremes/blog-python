from flask import Flask, request
import requests

app = Flask(__name__)


@app.post('/events')
def moderation_events_post():
    payload = request.json
    event_type = payload.get('type')
    data = payload.get('data')
    print(f"Received Event: {event_type}")

    if event_type == 'CommentCreated':
        status = 'rejected' if 'orange' in data.get('content') else 'approved'
        requests.post(url='http://event-bus-srv:4005/events', json={
            'type': 'CommentModerated',
            'data': {
                'id': data.get('id'),
                'post_id': data.get('post_id'),
                'status': status,
                'content': data.get('content')
            }

        })

    return {}, 200
