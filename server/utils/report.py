from pytz import timezone
from datetime import datetime

from bson import ObjectId

from server.core.db.databases import Color_db


def create_report(user_email: str, post_id: str, reason: str):
    db = Color_db()
    report_col = db.get_report_col()

    post = db.get_post_col().find_one({"_id": ObjectId(post_id)})
    feel = post["feel"]

    report_col.insert_one({
        "user_email": user_email,
        "post_id": ObjectId(post_id),
        "reason": reason,
        "feel": feel,
        "created_at": datetime.now(timezone("Asia/Seoul")).strftime("%Y-%m-%d %H:%M:%S")
    })
