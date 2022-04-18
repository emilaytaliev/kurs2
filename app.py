from flask import Flask, render_template, request, jsonify
from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, get_post,search_for_posts
from utils import load_post, get_posts_by_user

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



@app.route('/api/posts')
def api_posts():
    """Вывод всех постов в формате JSON"""
    posts = load_post()
    return jsonify(posts)


@app.route('/api/post/<int:uid>')
def api_post(uid):
    """Вывод одного поста в формате JSON"""
    post = get_posts_by_user(uid)
    return jsonify(post)



app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    app.run()