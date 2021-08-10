from fastapi import HTTPException, status

from bson import ObjectId

from server.core.db.databases import Color_db

from server.utils.post import get_post, get_comment, delete_post, delete_comment
from server.utils.user import get_user_nickname
from server.utils.user import delete_user


def get_post_report_detail(report_id: str):
    report = Color_db().get_report_col().find_one({"_id": ObjectId(report_id)})

    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="could not find report matching this id")

    reported_post = get_post(id=report["id"], type=report["type"])

    return {
        "post": reported_post,
        "report": {
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
            "user_email": report["user_email"],
            "user_nickname": get_user_nickname(report["user_email"]),
            "feel": report["feel"],
            "reason": report["reason"],
            "created_at": str(report["created_at"].strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))
        }
    }


def admin_delete(id: str, type: str):
    if type == "post":
        delete_post(post_id=id)
    elif type == "comment":
        delete_comment(comment_id=id)
    elif type == "user":
        delete_user(user_email=id)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="wrong type")
