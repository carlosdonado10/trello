from pydantic import BaseModel


class Member(BaseModel):
    id: str
    fullName: str
    username: str