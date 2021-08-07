from server.core.db.databases import Color_db


def get_user_nickname(user_email: str):
    user_col = Color_db().get_user_col()
    user = user_col.find_one({"_id": user_email})
    nickname = user["nickname"]

    return nickname
