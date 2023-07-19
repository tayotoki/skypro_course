import random as rd

from web_data_processing.html_parser import Parser
from basic_word import BasicWord

Parser.collect_data()
data = Parser.data_list


def load_random_word():
    random_word_data = rd.choice(data)

    return BasicWord(
        word=random_word_data.get("word"),
        subwords=random_word_data.get("subwords")
    )
