import webbrowser

from .get_link import get_link


def open_link(message: Exception, num_of_results: int = 1):
    for result in get_link(message, num_of_results):
        webbrowser.open_new_tab(result)
