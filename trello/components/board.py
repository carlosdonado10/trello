from datetime import datetime
from typing import List

from pydantic import BaseModel
import requests

from trello.components.card import Card
from trello.components.lists import TrelloList
from trello.constants import default_header
from trello.settings import settings
from trello.utils import check_valid_server_response


class Board(BaseModel):
    id: str
    name: str
    url: str

    @classmethod
    def get_user_boards(cls) -> List["Board"]:
        """
        Gets all the boards that can be accessed with the registered API Key
        see: https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/
        :return: list of boards
        """

        response = requests.request(
            "GET",
            'https://api.trello.com/1/members/me/boards?fields=name,url',
            headers=default_header,
            params=settings.get_auth_query_params()
        )

        check_valid_server_response(response, "get user boards")

        return [Board(**board_data) for board_data in response.json()]

    @classmethod
    def get_board_by_id(cls, board_id: str) -> "Board":
        response = requests.request(
            "GET",
            f'https://api.trello.com/1/boards/{board_id}',
            headers=default_header,
            params=settings.get_auth_query_params()
        )

        check_valid_server_response(response, f"get board by id: {board_id}")

        return Board(**response.json())

    def get_board_cards(self) -> List[Card]:
        response = requests.request(
            "GET",
            f"https://api.trello.com/1/boards/{self.id}/cards",
            headers=default_header,
            params=settings.get_auth_query_params()
        )

        check_valid_server_response(response, f'get all cards in the board: {self.id}')

        return [Card(**card_data) for card_data in response.json()]

    def get_lists_on_a_board(self) -> List[TrelloList]:
        response = requests.request(
            "GET",
            f"https://api.trello.com/1/boards/{self.id}/lists",
            headers=default_header,
            params=settings.get_auth_query_params()
        )

        check_valid_server_response(response, f'get all lists in the board: {self.id}')

        return [TrelloList(**list_data) for list_data in response.json()]

    def get_board_members(self) -> List:
        response = requests.request(
            "GET",
            f"https://api.trello.com/1/boards/{self.id}/members",
            headers=default_header,
            params=settings.get_auth_query_params()
        )

        check_valid_server_response(response, f'get all members in the board: {self.id}')

        return response.json()


    def create_card(self, cards: List[Card], list_id: str) -> None:
        """
        Creates new cards in the Board given by parameter
        see: https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post
        :param list_id: ID of the list to add the card to (list=columns of the board)
        :param cards:
        :return:
        """

        for card in cards:

            query_params = {**settings.get_auth_query_params(), **{k: v for k ,v in card.dict().items() if v is not None}, 'idList': list_id.id}

            response = requests.request(
                "POST",
                "https://api.trello.com/1/cards",
                headers=default_header,
                params=query_params
            )

            check_valid_server_response(response, "Create card\n cards created: [] cards missing: []")


if __name__ == '__main__':
    Board.get_user_boards()
    b = Board.get_board_by_id('65bc0953a7d711283ea7a2a8')
    b.get_board_members()

    # print("Current cards: ")
    # print(b.get_board_cards())
    # lists = b.get_lists_on_a_board()
    # dict_of_t_lists = {t_list.name: t_list for t_list in lists}
    # b.create_card([Card(name='C1', desc="Primera mejora de crudos", idMembers=[], due=None, shortUrl=None, id=None)], list_id=dict_of_t_lists['Backlog'])
