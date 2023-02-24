# from dataclasses import dataclass
# from typing import Dict, Sequence

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# @dataclass
# class Comment:
#     id: str
#     content: str
#     status: str

# @dataclass()
# class Post:
#     id: str
#     title: str
#     comments: Sequence[Comment]


# posts: Dict[str, Post] = {}
posts = {}


@app.get('/posts')
def query_posts_get():
    return posts, 200


@app.post('/events')
def query_events_post():
    payload = request.json
    event_type = payload.get('type')
    data = payload.get('data')
    print(f"Received Event: {event_type}")

    if event_type == 'PostCreated':
        post_id = data.get('id')
        title = data.get('title')
        posts[post_id] = {'id': post_id, 'title': title, 'comments': []}
    if event_type == 'CommentCreated':
        comment_id = data.get('id')
        content = data.get('content')
        post_id = data.get('post_id')
        status = data.get('status')
        post = posts[post_id]
        post['comments'].append({'id': comment_id, 'content': content, 'status': status})
    if event_type == 'CommentUpdated':
        comment_id = data.get('id')
        content = data.get('content')
        post_id = data.get('post_id')
        status = data.get('status')
        post = posts[post_id]
        comment = next((comment for comment in post['comments'] if comment['id'] == comment_id), None)
        comment['status'] = status
        comment['content'] = content

    print(posts)
    return {}, 200

