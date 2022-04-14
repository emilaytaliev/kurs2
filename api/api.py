from flask import Blueprint, jsonify
from utils import load_post, get_posts_by_user
POSTS = 'data/data.json'
api = Blueprint('api', __name__)


@api.route('/api/posts')
def api_posts():
	"""Вывод всех постов в формате JSON"""
	posts = load_post(POSTS)
	return jsonify(posts)


@api.route('/api/post/<int:uid>')
def api_post(uid):
	"""Вывод одного поста в формате JSON"""
	posts = load_post(POSTS)
	post = get_posts_by_user(posts, uid)
	return jsonify(post)