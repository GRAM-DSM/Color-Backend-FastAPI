from fastapi import HTTPException, status

from pymongo.collection import Collection

from bson.objectid import ObjectId

from server.core.db.databases import Color_db

# from server.utils.notify import get_user_fcm_tokens_from_post, send_message
# from server.utils.user import get_user_nickname


def is_like(post_col: Collection, user_email: str, post_id: str):
    if not (post := post_col.find_one({"_id": ObjectId(post_id)})):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="could not find matching post id")

    like_list = post["favorite"]

    return True if user_email in like_list else False


def like(post_col: Collection, user_email: str, post_id: str):
    post_col.update_one({"_id": ObjectId(post_id)}, {"$push": {"favorite": user_email}})

    # nickname = get_user_nickname(user_email=user_email)
    # token = get_user_fcm_tokens_from_post(post_id=post_id)
    # send_message(token=token, body=f"{nickname}님이 회원님의 게시물을 좋아합니다")


def unlike(post_col: Collection, user_email: str, post_id: str):\
    post_col.update_one({"_id": ObjectId(post_id)}, {"$pull": {"favorite": user_email}})


def like_it(user_email: str, post_id: str):
    post_col = Color_db().get_post_col()

    if is_like(post_col=post_col, user_email=user_email, post_id=post_id):
        unlike(post_col=post_col, user_email=user_email, post_id=post_id)
    else:
        like(post_col=post_col, user_email=user_email, post_id=post_id)
