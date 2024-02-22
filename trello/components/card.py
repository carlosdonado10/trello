import json
from datetime import datetime
from typing import List, Optional

import requests
from pydantic import BaseModel

from trello.components.custom_field import CustomField
from trello.constants import default_header
from trello.settings import settings
from trello.utils import check_valid_server_response


class Card(BaseModel):
    id: Optional[str]
    name: str
    desc: str
    due: Optional[datetime]
    shortUrl: Optional[str]
    idMembers: List[str]
    idList: Optional[str]

    def update_custom_field(self, custom_field: CustomField):
        """

        :param custom_fields:
        :return:
        """
        payload = json.dumps({'idValue': custom_field.idValue})

        response = requests.request(
            "PUT",
            f'https://api.trello.com/1/cards/{self.id}/customField/{custom_field.idCustomField}/item',
            headers=default_header,
            params=settings.get_auth_query_params(),
            data=payload
        )

        check_valid_server_response(response, f'Updating custom fields in card: {self.id}')
