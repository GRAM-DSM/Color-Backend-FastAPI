from fastapi import HTTPException, status

from pymongo.collection import Collection

from server.core.db.databases import Color_db

from server.utils.post import get_user_posts


def is_my_profile(user_email: str, user: dict):
    return True if user_email == user["_id"] else False


def get_user_profile(user_email: str, page_id: str, feel: str, filter: str, page: int):
    user = Color_db().get_user_col().find_one({"_id": page_id})

    posts = get_user_posts(user_email=user_email, page_id=page_id, feel=feel, filter=filter, page=page)

    return {
        "user_info": {
            "nickname": user["nickname"],
            "is_mine": is_my_profile(user_email=user_email, user=user)
        },
        "posts": posts
    }


def is_nickname_in_use(nickname: str, user_col: Collection):
    user = user_col.find_one({"nickname": nickname})

    return True if user else False


def change_nickname(user_email: str, nickname: str):
    user_col = Color_db().get_user_col()

    if is_nickname_in_use(nickname=nickname, user_col=user_col):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="this nickname is already in use")

    user_col.update_one({"_id": user_email}, {"$set": {"nickname": nickname}})
