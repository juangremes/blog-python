from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

posts = {}


@app.get('/posts')
def query_posts_get():
    return posts, 200


@app.post('/events')
def query_events_post():
    payload = request.json
    event_type = payload.get('type')
    data = payload.get('data')

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

    print(posts)
    return {}, 200

