import webbrowser
import requests


def create_query(message) -> str:
    if isinstance(message, Exception):
        return type(message).__name__ + ": " + str(message)
    elif isinstance(message, str):
        return message
    raise TypeError("query must be a string or exception")

def create_tags(tags: list) -> str:
    tags_string = ""
    for tag in tags:
        tags_string += f"{tag};"
    return tags_string

def get_links(message, tags: list = ["python"], num_of_results: int = 5) -> list:
    query = create_query(message)
    tags = create_tags(tags)
    link = f"https://api.stackexchange.com//2.2/similar?order=desc&sort=relevance&tagged={tags}&title={query}&site=stackoverflow"
    response = requests.get(link)
    return [result["link"] for result in response.json()["items"][0:num_of_results]]

def open_links(message: Exception, num_of_results: int = 1) -> None:
    for result in get_links(message, num_of_results=num_of_results):
        webbrowser.open_new_tab(result)
