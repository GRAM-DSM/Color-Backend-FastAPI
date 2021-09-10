from fastapi import HTTPException, status

from bson import ObjectId

from server.core.db.databases import Color_db

from server.utils.post import get_post, get_comment
from server.utils.user import get_user_nickname


def get_post_report_detail(report_id: str):
    report = Color_db().get_report_col().find_one({"_id": ObjectId(report_id)})

    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="could not find report matching this id")

    reported_post = get_post(id=report["id"], type=report["type"])

    return {
        "post": reported_post,
        "report": {
            "report_id": str(report["_id"]),
            "user_email": report["user_email"],
            "user_nickname": get_user_nickname(report["user_email"]),
            "feel": report["feel"],
            "reason": report["reason"],
            "created_at": str(report["created_at"].strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))
        }
    }


def get_comment_report_detail(report_id: str):
    report = Color_db().get_report_col().find_one({"_id": ObjectId(report_id)})

    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="could not find report matching this id")


    commented_post = get_post(id=report["id"], type=report["type"])
    reported_comment = get_comment(comment_id=report["id"])

    return {
        "post": commented_post,
        "comment": reported_comment,
        "report": {
            "report_id": str(report["_id"]),
            "user_email": report["user_email"],
            "user_nickname": get_user_nickname(report["user_email"]),
            "feel": report["feel"],
            "reason": report["reason"],
            "created_at": str(report["created_at"].strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))
        }
    }
