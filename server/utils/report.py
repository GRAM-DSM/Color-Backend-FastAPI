from pymongo.collection import Collection

from pytz import timezone
from datetime import datetime

from bson import ObjectId

from server.core.db.databases import Color_db

from server.utils.user import get_user_nickname


def create_report(user_email: str, id: str, reason: str, feel: str, type: str):
    report_col = Color_db().get_report_col()

    report_col.insert_one({
        "user_email": user_email,
        "id": id,
        "reason": reason,
        "feel": feel,
        "type": type,
        "created_at": datetime.now(timezone("Asia/Seoul"))
    })


def get_reports_count(report_col: Collection):
    post_report_cnt = report_col.count({"type": "post"})
    comment_report_cnt = report_col.count({"type": "comment"})

    return post_report_cnt, comment_report_cnt


def get_reports(type: str, page: int):
    report_col = Color_db().get_report_col()

    reports = report_col.find({"type": type}).skip((page - 1) * 10).limit(10)

    post_report_cnt, comment_report_cnt = get_reports_count(report_col=report_col)

    return {
        "post_report_count": post_report_cnt,
        "comment_report_count": comment_report_cnt,
        "reports": [{
            "report_id": str(report["_id"]),
            "feel": report["feel"],
            "reporter_nickname": get_user_nickname(report["user_email"]),
            "created_at": str(report["created_at"].strftime("%Y년 %m월 %d일")),
            "reason": report["reason"]
        } for report in reports ]
    }


def delete_reports(reported_obj_id: str):
    Color_db().get_report_col().delete_many({"id": reported_obj_id})


def delete_report(report_id: str):
    report_col = Color_db().get_report_col()

    reported_obj_id = report_col.find_one({"_id": ObjectId(report_id)})["id"]
    delete_reports(reported_obj_id=reported_obj_id)
