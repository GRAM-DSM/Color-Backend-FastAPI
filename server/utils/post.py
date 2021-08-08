import pymongo

from server.core.db.databases import Color_db


def get_user_posts(user_email: str, page_id: str, feel: str, filter: str, page: int):
    post_col = Color_db().get_post_col()
    posts = []

    if filter == "post":
        posts = post_col.find({"$and": [{"userEmail": page_id}, {"feel": feel}]})\
            .sort("createdAt", pymongo.DESCENDING)\
            .skip((page-1)*10).limit(10)
    elif filter == "like":
        posts = post_col.find({"$and": [{"favorite": [page_id]}, {"feel": feel}]})\
            .sort("createdAt", pymongo.DESCENDING)\
            .skip((page-1)*10).limit(10)

    return [{
        "id": str(post["_id"]),
        "content": post["content"],
        "is_mine": True if post["userEmail"] == user_email else False,
        "created_at": str(post["createdAt"].strftime("%Y년 %m월 %d일")),
        "user_nickname": post["nickname"],
        "comment_cnt": len(post["comment"]),
        "favorite_cnt": len(post["favorite"]),
        "is_favorite": True if user_email in post["favorite"] else False,
        "hash_tag": post["hashTag"]
    } for post in posts]
