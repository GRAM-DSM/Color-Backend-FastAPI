from fastapi import HTTPException, status

from pymongo import DESCENDING

from bson import ObjectId

from server.core.db.databases import Color_db

from server.utils.report import delete_reports


def get_user_posts(user_email: str, page_id: str, feel: str, filter: str, page: int):
    post_col = Color_db().get_post_col()
    posts = []

    if filter == "post":
        posts = post_col.find({"$and": [{"userEmail": page_id}, {"feel": feel}]})\
            .sort("createdAt", DESCENDING)\
            .skip((page-1)*10).limit(10)
    elif filter == "like":
        posts = post_col.find({"$and": [{"favorite": [page_id]}, {"feel": feel}]})\
            .sort("createdAt", DESCENDING)\
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


def get_post(id: str, type: str):
    if type == "post":
        post = Color_db().get_post_col().find_one({"_id": ObjectId(id)})
    elif type == "comment":
        post = Color_db().get_post_col().find_one({"comment": {"$elemMatch": {"_id": id}}})
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="wrong type")

    return {
        "id": str(id),
        "nickname": post["nickname"],
        "created_at": str(post["createdAt"].strftime("%Y년 %m월 %d일")),
        "content": post["content"]
    }


def get_comment(comment_id: str):
    post = Color_db().get_post_col().find_one({"comment": {"$elemMatch": {"_id": comment_id}}})
    comment = list(filter(lambda com: com["_id"] == comment_id, post["comment"]))[0]

    return {
        "id": comment_id,
        "user_nickname": comment["userNickname"],
        "created_at": str(comment["createdAt"].strftime("%Y년 %m월 %d일")),
        "content": comment["content"]
    }


def delete_post(post_id: str):
    Color_db().get_post_col().delete_one({"_id": ObjectId(post_id)})
    delete_reports(reported_obj_id=post_id)


def delete_comment(comment_id: str):
    post_col = Color_db().get_post_col()

    post = post_col.find_one({"comment": {"$elemMatch": {"_id": comment_id}}})
    del_comment = list(filter(lambda com: com["_id"] == comment_id, post["comment"]))[0]

    post_col.update_one({"comment": {"$elemMatch": {"_id": comment_id}}}, {"$pull": {"comment": del_comment}})
    delete_reports(reported_obj_id=comment_id)
