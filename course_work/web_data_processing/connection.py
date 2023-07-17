from typing import Generator, Any

import requests
from fake_useragent import UserAgent

from course_work.settings import WORDS

url = "https://wordhelp.ru/search"

user_agent = UserAgent().random

payloads = [
    {
        "a": "combination",
        "utf8": "☃",
        "word": f"{word}",
    } for word in WORDS
]

headers = {
    "User-Agent": f"{user_agent}"
}


def get_page():
    with requests.Session() as session:  # type: requests.Session
        for payload in payloads:
            response: requests.Response = session.post(url=url, headers=headers, data=payload)

            if response.status_code == 200:
                yield payload["word"], response.text


pages_generator: Generator[tuple[str, str], Any, None] = get_page()
