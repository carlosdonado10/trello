from typing import List

from pydantic import BaseModel


class CustomFieldOption(BaseModel):
    id: str
    value: str


class CustomField(BaseModel):
    id: str
    name: str
    options: List[CustomFieldOption]


class SelectedValue(BaseModel):
    text: str


class CustomFieldUpload(BaseModel):
    idCustomField: str
    value: SelectedValue
    idValue: str



