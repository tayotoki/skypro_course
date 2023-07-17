from typing import Optional

from utils import load_random_word
from players import Player
from basic_word import BasicWord
from settings import MAX_WORDS_AMOUNT


class Game:
    def __init__(self, rounds_amount: int = MAX_WORDS_AMOUNT):
        self.player: Optional[Player] = None
        self.word: BasicWord = load_random_word()
        self.rounds_amount: int = (
            rounds_amount
            if len(self.word) >= MAX_WORDS_AMOUNT
            else len(self.word)
        )
        self.stop_words = [
            "stop",
            "конец",
            "стоп",
            "выход",
            "quit",
            "exit",
            "хватит",
            "закончили",
            "прекрати",
            "ямате кудасай",
            "спасите",
        ]

    def start(self):
        username = input(
            "Введите имя игрока\n"
        )

        self.player = Player(username)

        print(
            f"Составьте {self.rounds_amount}"
            f" слов из слова {self.word}\n"
            f"Слова должны быть не короче 3"
            f" букв\nЧтобы закончить игру,"
            f" угадайте все слова или напишите 'stop'\n"
            f"Поехали, ваше первое слово?\n"
        )

        player_word = ''

        while (
            player_word not in self.stop_words
        ) and (
            len(self.player) < self.rounds_amount
        ):
            player_word = input().strip().lower()

            if self.word.is_correct(player_word):
                if not self.player.is_used(player_word):
                    print("верно")
                    self.player.add(player_word)
                else:
                    print("уже использовано")
            else:
                print("неверно")

        print(f"Игра завершена, вы угадали {len(self.player)} слов!")


def main():
    Game().start()


if __name__ == "__main__":
    main()
