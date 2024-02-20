from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Card(BaseModel):
    id: Optional[str]
    name: str
    desc: str
    due: Optional[datetime]
    shortUrl: Optional[str]
    idMembers: List[str]

