from server.core.db.databases import Color_db


def get_user_nickname(user_email: str):
    user_col = Color_db().get_user_col()
    user = user_col.find_one({"_id": user_email})
    nickname = user["nickname"]

    return nickname


def delete_user(user_email: str):
    db = Color_db()
    user_col = db.get_user_col()
    post_col = db.get_post_col()

    user_col.delete_one({"_id": user_email})
    post_col.delete_many({"userEmail": user_email})
