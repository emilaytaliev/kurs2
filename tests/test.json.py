from flask import Flask, jsonify
from utils import load_post, get_posts_by_user
app = Flask(__name__)

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