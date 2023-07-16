from typing import Any, Optional

from bs4 import BeautifulSoup
from connection import pages_generator


class Parser:
    parser: BeautifulSoup = BeautifulSoup
    generator = pages_generator
    words_storage: Optional[list[dict[str, str | list[str]]]] = None

    @classmethod
    def collect_data(cls) -> None:
        for word, page in cls.generator:
            cls.add_to_storage(
                {
                    "word": word,
                    "subwords": cls.parse_words(from_ := page),
                }
            )

    @classmethod
    def parse_words(cls, page: str | Any | None) -> list[str]:
        buffer = []

        if page is not None:
            soup = cls.parser(page, "html.parser")
            words = soup.find_all(
                "ul", {"class": "list-inline results"}
            )
            for word in words:
                current_word = word.find("a").string

                if len(current_word) > 3:
                    buffer.append(current_word)

        return buffer

    @classmethod
    def add_to_storage(cls, data: dict):
        if cls.words_storage is None:
            cls.words_storage = []

        cls.words_storage.append(data)



Parser.collect_data()

print(Parser.words_storage)