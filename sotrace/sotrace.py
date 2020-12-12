from http import HTTPStatus
from typing import Any, List, Union, Optional
import webbrowser

import requests


__all__ = (
    'get_links',
    'open_links',
)


def create_query(message: Union[str, BaseException]) -> str:
    '''
    Generates the query to stackoverflow's API based on the message

    :param message: A message to generate the query from,
    can be an exception or a string
    :type message: Union[str, BaseException]
    :raises TypeError: If the message is neither an exception nor a string
    :return: The computed query
    :rtype: str
    '''

    if isinstance(message, BaseException):
        return type(message).__name__ + ": " + str(message)
    elif isinstance(message, str):
        return message
    raise TypeError(
        f"Query must be a string or exception, not {type(message)}"
    )


def create_tags(tags: List[Any]) -> str:
    '''
    Creates a string with all the supplied tags

    :param tags: A list of tags to add to the query
    :type tags: List[Any]
    :return: A `;` separated list of tags
    :rtype: str
    '''
    return ';'.join(tags)


def get_links(
        message: Union[str, BaseException],
        tags: Optional[List[str]] = None,
        num_of_results: int = 5
        ) -> list:
    '''
    Gets the links for a specific query, or exception from the StackOverflow
    API.

    :param message: The query as a string, or an exception to look up
    :type message: Union[str, BaseException]
    :param tags: A list of tags to restrict the query to, defaults to None
    :type tags: Optional[List[str]], optional
    :param num_of_results: The number of results to
    return from SO's API, defaults to 5
    :type num_of_results: int, optional
    :raises: message, if stackoverflow is down,
    or the API has changed its routes.
    :return: A list of question URLs matching the query/exception.
    :rtype: List[str]
    '''

    if tags is None:
        tags = ['python']

    query = create_query(message)
    tags = create_tags(tags)
    link = (
        f"https://api.stackexchange.com/2.2/similar"
        f"?order=desc&sort=relevance"
        f"&tagged={tags}&title={query}&site=stackoverflow"
    )
    response = requests.get(link)
    if response.status_code == HTTPStatus.OK:
        return [
            result["link"]
            for result in response.json()["items"][0:num_of_results]
        ]
    elif isinstance(message, BaseException):
        raise message


def open_links(
        message: Union[str, BaseException],
        tags: Optional[List[str]] = None,
        num_of_results: int = 1
        ) -> None:
    '''
    Opens stackoverflow links in the browser based on the message

    :param message: A message, either a string or an exception
    to look for on SO
    :type message: Union[str, BaseException]
    :param tags: A list of tags to restrict the query to, defaults to None
    :type tags: Optional[List[str]], optional
    :param num_of_results: The number of results to open, defaults to 1
    :type num_of_results: int, optional
    '''

    for result in get_links(message, tags=tags, num_of_results=num_of_results):
        webbrowser.open_new_tab(result)
