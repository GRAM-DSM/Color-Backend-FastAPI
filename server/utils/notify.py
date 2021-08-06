from pyfcm import FCMNotification

from bson import ObjectId

from server.core.db.databases import Color_db

from server.config import APIKEY


push_service = FCMNotification(APIKEY)


def get_user_fcm_tokens_from_post(post_id: str):
    color_db = Color_db()

    post_col = color_db.get_post_col()
    post = post_col.find_one({"_id": ObjectId(post_id)})
    user_email = post["userEmail"]

    user_col = color_db.get_user_col()
    user = user_col.find_one({"_id": user_email})
    token = user["deviceToken"]

    return token


def send_message(token: str, body: str):
    message = {
        "body": body,
        "click_action": "like"
    }

    push_service.notify_single_device(
        registration_id=token,
        data_message=message
    )
