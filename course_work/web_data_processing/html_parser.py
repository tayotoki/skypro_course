import json
from typing import Any, Optional

from bs4 import BeautifulSoup

from .connection import pages_generator


class Parser:
    parser: BeautifulSoup = BeautifulSoup
    generator = pages_generator
    data_list: Optional[list[dict[str, str | list[str]]]] = None

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

        if page is not None and isinstance(page, str):
            soup = cls.parser(page, "html.parser")
            words = soup.find_all(
                "ul", {"class": "list-inline results"}
            )
            for words_ in words:
                current_words = words_("a")

                for subword in current_words:  # noqa
                    subword = subword.string  # noqa

                    if len(subword) > 2:
                        buffer.append(subword)

        return buffer

    @classmethod
    def add_to_storage(cls, data: dict):
        if cls.data_list is None:
            cls.data_list = []

        cls.data_list.append(data)


if __name__ == "__main__":
    Parser.collect_data()
    print(json.dumps(Parser.data_list, indent=2, ensure_ascii=False))
