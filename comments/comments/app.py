import uuid
from typing import Dict

import requests
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

comments_by_post_id: Dict[str, list] = {}
# { post_id: Comment[] }


@app.get('/posts/<post_id>/comments')
def comments_get(post_id):
    return comments_by_post_id.get(post_id) or [], 200


@app.post('/posts/<post_id>/comments')
def comments_post(post_id):
    # if comments_by_post_id.get(post_id) is None:
    #    return 'Post ID not found', 404
    data = request.json
    comment_id = uuid.uuid1().hex
    content = data.get('content')
    comments = comments_by_post_id.get(post_id) or []
    comments.append({'id': comment_id, 'content': content, 'status': 'pending'})
    comments_by_post_id[post_id] = comments
    requests.post(url='http://localhost:4005/events', json={
        'type': 'CommentCreated',
        'data': {
            'id': comment_id,
            'content': content,
            'post_id': post_id,
            'status': 'pending'
        }
    })
    return comments, 201


@app.post('/events')
def comments_receive_events_post():
    print(f"Received Event {request.json.get('type')}")
    return {}, 200
