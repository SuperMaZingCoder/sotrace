import requests


def get_link(message: Exception, num_of_results: int = 5):
    print(type(num_of_results))
    query = type(message).__name__ + ": " + str(message)
    response = requests.get(f"https://api.stackexchange.com//2.2/similar?order=desc&sort=relevance&tagged=python&title={query}&site=stackoverflow")
    return [result["link"] for result in response.json()["items"][0:num_of_results]]
