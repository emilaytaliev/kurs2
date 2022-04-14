import json


#Посты вместе с информацией
def load_post():
    with open('data/data.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


#комментарий
def load_comment():
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comment = json.load(file)
    return comment


#возвращает посты
def get_posts_all():

    return load_post()


#возвращает один пост по его идентификатору
def get_posts_by_user(user_name):
    post = []
    for i in load_post():
        if user_name == i['pk']:
            post.append(i)
    return post


#возвращает посты определенного пользователя
def get_post(user):
    post = []
    for i in load_post():
        if user == i['poster_name']:
            post.append(i)
    return post


#возвращает комментарии определенного поста
def get_comments_by_post_id(post_id):
    coment = []
    for i in load_comment():
        if post_id == i['post_id']:
            coment.append(i)
    return coment


#возвращает список постов по ключевому слову
def search_for_posts(query):
    all_posts = [x for x in load_post() if query in x['content']]
    return all_posts[:10]


#возвращает один пост по его идентификатору
def get_post_by_pk(pk):
    for i in load_post():
        if pk == i['pk']:
            return {
                'poster_name': i['poster_name'],
                "poster_avatar": i["poster_avatar"],
                "pic": i["pic"],
                "content": i["content"],
                "views_count": i["views_count"],
                "likes_count": i["likes_count"],
                "pk": i["pk"],
            }



