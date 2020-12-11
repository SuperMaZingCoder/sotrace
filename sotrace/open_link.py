import webbrowser

from .get_link import get_link


def open_link(message: Exception):
    webbrowser.open_new_tab(get_link(message, 1))
