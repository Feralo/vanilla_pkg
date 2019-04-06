from urllib.parse import urljoin
import requests

BASE_URL = "http://jsonplaceholder.typicode.com"

TODOS_URL = urljoin(BASE_URL, "todos")


def get_todos():
    response = requests.get(TODOS_URL)
    if response.ok:
        return response
    else:
        return None
