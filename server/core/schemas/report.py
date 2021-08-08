from pydantic import BaseModel


class Report(BaseModel):
    reason: str
    feel: str
