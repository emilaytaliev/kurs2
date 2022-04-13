from flask import Flask, render_template, request
from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, get_post,search_for_posts
app = Flask(__name__)

@app.route("/")
def index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts, len=len(posts))


@app.route("/post/<int:name>")
def post(name):
    posts = get_posts_by_user(name)
    comment = get_comments_by_post_id(name)
    return render_template('post.html', posts=posts, len=len(comment), comment=comment)


@app.route("/user-feed/<user>")
def feed(user):
    feeds = get_post(user)
    return render_template('user-feed.html', feeds=feeds)


@app.route("/search/")
def search():
    search_by = request.args.get("s")
    posts = search_for_posts(search_by)
    return render_template('search.html', search_by=search_by, posts=posts, len=len(posts))




app.run(debug=True)