from typing import Optional

from fastapi import APIRouter, status, Header

from server.utils import decode_token
from server.utils.like import like_it


router = APIRouter()


@router.put("/like/", status_code=status.HTTP_200_OK, tags=["like"])
async def like(post_id: str, Authorization: Optional[str] = Header(None)):
    user_email = decode_token(token=Authorization)

    like_it(user_email=user_email, post_id=post_id)

    return {
        "message": "success"
    }
