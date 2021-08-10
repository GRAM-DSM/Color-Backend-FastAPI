from fastapi import APIRouter, status

from server.utils.report import get_reports
from server.utils.admin import get_post_report_detail, get_comment_report_detail, admin_delete


router = APIRouter()


@router.get("/admin", status_code=status.HTTP_200_OK, tags=["admin"])
async def admin_main(type: str, page: int):
    reports = get_reports(type=type, page=page)

    return reports


@router.get("/admin/post/{report_id}", status_code=status.HTTP_200_OK, tags=["admin"])
async def post_report_detail(report_id: str):
    report = get_post_report_detail(report_id=report_id)

    return report


@router.get("/admin/comment/{report_id}", status_code=status.HTTP_200_OK, tags=["admin"])
async def post_report_detail(report_id: str):
    report = get_comment_report_detail(report_id=report_id)

    return report


@router.delete("/admin/{type}/{id}", status_code=status.HTTP_200_OK, tags=["admin"])
async def delete(type: str, id: str):
    admin_delete(id=id, type=type)

    return {
        "message": "success"
    }
