import random as rd
import re

from pathlib import Path
from typing import Generator


BASE_DIR: Path = Path(__file__).resolve().parent

CONFIG = {
    "DATA_FILE": BASE_DIR / "words.txt",
    "HISTORY_FILE": BASE_DIR / "history.txt",
}

class FilesHandler:
    data_file_path: Path = CONFIG.get("DATA_FILE")
    file_for_write: Path = CONFIG.get("HISTORY_FILE")

    @classmethod
    def get_file_rows(
        cls,
        file_path: str | Path = None,
    ) -> Generator[str, None, None]:

        if file_path is None:
            file_path = cls.data_file_path

        with open(file_path, "r") as file:
            while True:
                line = file.readline().strip()

                if not line:
                    break

                yield line

    @classmethod
    def write_to_file(cls,
                      data_strings: tuple[str],
                      *,
                      is_rewrite: bool = False) -> None:

        mode = "a" if not is_rewrite else "w"

        try:
            iter(data_strings)
        except TypeError:
            data_strings = (data_strings, )
        else:
            if isinstance(data_strings, (str, bytes)):
                data_strings = (data_strings.strip(), )

        with open(
            cls.file_for_write,
            mode=mode,
            encoding="utf-8",
        ) as file:
            file.writelines(data_strings)


class Game:
    def __init__(self) -> None:
        self.points = 0
        self.username = None
        self.file_handler = FilesHandler

    def start_chat(self):
        self.username = input("Введите ваше имя\n")

        for row in self.file_handler.get_file_rows():
            user_answer = input(
                f"Угадайте слово {self.get_shuffle_word(row)}\n"
            )

            if user_answer == row:
                print("Верно! Вы получаете 10 очков.")
                self.points += 10
            else:
                print(f"Неверно! Верный ответ – {row}")

        self.file_handler.write_to_file((f" {self.username} {self.points}\n",))
        self.show_stats()

    @staticmethod
    def get_shuffle_word(word: str) -> str:
        word = list(word)
        rd.shuffle(word)

        return "".join(word)

    def show_stats(self):
        history_file = self.file_handler.file_for_write
        all_text = "".join(list(self.file_handler.get_file_rows(history_file)))

        user_games = re.findall(
                        f"(?:({self.username}) (\\d+))",
                        all_text,
                    )

        max_points_record = max(user_games, key=lambda x: int(x[1]))

        print(f"Всего игр сыграно: {len(user_games)}\n"
              f"Максимальный рекорд: {max_points_record[1]}")


def main():
    Game().start_chat()


if __name__ == "__main__":
    main()
