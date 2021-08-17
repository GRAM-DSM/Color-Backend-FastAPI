from fastapi import APIRouter, status

from server.utils.report import get_reports, delete_report
from server.utils.admin import get_post_report_detail, get_comment_report_detail
from server.utils.post import delete_post, delete_comment
from server.utils.user import delete_user


router = APIRouter()


@router.get("/admin", status_code=status.HTTP_200_OK, tags=["admin"])
async def admin_main(type: str, page: int):
    reports = get_reports(type=type, page=page)

    return reports


@router.get("/admin/post", status_code=status.HTTP_200_OK, tags=["admin"])
async def post_report_detail(report_id: str):
    report = get_post_report_detail(report_id=report_id)

    return report


@router.get("/admin/comment", status_code=status.HTTP_200_OK, tags=["admin"])
async def post_report_detail(report_id: str):
    report = get_comment_report_detail(report_id=report_id)

    return report


@router.delete("/admin/report", status_code=status.HTTP_200_OK, tags=["admin"])
async def delete_reports(report_id: str):
    delete_report(report_id=report_id)

    return {
        "message": "success"
    }


@router.delete("/admin/post", status_code=status.HTTP_200_OK, tags=["admin"])
async def delete_post_reports(post_id: str):
    delete_post(post_id=post_id)

    return {
        "message": "success"
    }


@router.delete("/admin/comment", status_code=status.HTTP_200_OK, tags=["admin"])
async def delete_comment_reports(comment_id: str):
    delete_comment(comment_id=comment_id)

    return {
        "message": "success"
    }


@router.delete("/admin/user", status_code=status.HTTP_200_OK, tags=["admin"])
async def delete_user_posts(user_email: str):
    delete_user(user_email=user_email)

    return {
        "message": "success"
    }
