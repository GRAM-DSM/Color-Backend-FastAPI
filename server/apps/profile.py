from fastapi import APIRouter, status, Header

from typing import Optional

from server.core.schemas.profile import Update_nickname

from server.utils import decode_token
from server.utils.profile import get_user_profile, change_nickname


router = APIRouter()


@router.get("/profile", status_code=status.HTTP_200_OK, tags=["profile"])
async def my_page(id: str, feel: str, filter: str, page: int, Authorization: Optional[str] = Header(None)):
    user_email = decode_token(token=Authorization)

    profile = get_user_profile(user_email=user_email, page_id=id, feel=feel, filter=filter, page=page)

    return profile


@router.put("/profile", status_code=status.HTTP_200_OK, tags=["profile"])
async def update_nickname(body: Update_nickname, Authorization: Optional[str] = Header(None)):
    user_email = decode_token(token=Authorization)

    change_nickname(user_email=user_email, nickname=body.nickname)

    return {
        "message": "success"
    }
