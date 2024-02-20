from pydantic import BaseModel


class TrelloList(BaseModel):
    id: str
    name: str
