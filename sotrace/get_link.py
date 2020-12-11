import requests


def get_link(message: Exception, num_of_results: int = 5):
    query = type(message).__name__ + ": " + str(message)
    result = requests.get(f"https://api.stackexchange.com//2.2/similar?order=desc&sort=relevance&tagged=python&title={query}&site=stackoverflow")
    return result.json()["items"][0:num_of_results]["link"]
