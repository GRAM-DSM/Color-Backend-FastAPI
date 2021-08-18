from fastapi import HTTPException, status

import jwt

from server.config import SECRET_KEY, ALGORITHM


def decode_token(token):
    try:
        payload = jwt.decode(token[7:], SECRET_KEY, algorithms=[ALGORITHM])
        if (payload["type"] == "access"):
            return payload["sub"]
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="access token is required")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token")
