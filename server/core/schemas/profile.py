from pydantic import BaseModel, constr


class Update_nickname(BaseModel):
    nickname: constr(min_length=1)
