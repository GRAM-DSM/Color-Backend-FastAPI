from fastapi import APIRouter, status, Header

from typing import Optional

from server.core.schemas.report import Report

from server.utils import decode_token
from server.utils.report import create_report


router = APIRouter()


@router.post("/report/", status_code=status.HTTP_201_CREATED, tags=["report"])
async def report(body: Report, post_id: str, Authorization: Optional[str] = Header(None)):
    user_email = decode_token(token=Authorization)

    create_report(user_email=user_email, post_id=post_id, reason=body.reason)

    return {
        "message": "success"
    }
