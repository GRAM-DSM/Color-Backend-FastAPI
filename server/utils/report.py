from pytz import timezone
from datetime import datetime

from bson import ObjectId

from server.core.db.databases import Color_db


def create_report(user_email: str, id: str, reason: str, feel: str, type: str):
    db = Color_db()
    report_col = db.get_report_col()

    report_col.insert_one({
        "user_email": user_email,
        "id": ObjectId(id),
        "reason": reason,
        "feel": feel,
        "type": type,
        "created_at": datetime.now(timezone("Asia/Seoul")).strftime("%Y-%m-%d %H:%M:%S")
    })
