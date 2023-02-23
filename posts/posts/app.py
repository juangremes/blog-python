import uuid

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

posts = {}


@app.get('/posts')
def posts_get():
    return posts, 200


@app.post('/posts')
def posts_post():
    data = request.json
    id = uuid.uuid1().hex
    title = data.get('title')
    print(id)
    posts[id] = {'id': id, 'title': title}
    print(posts[id])
    return posts[id], 201
