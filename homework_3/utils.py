from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from decorators import shuffle

GRADE = 5  # Max difficulty grade.
BASE_DIR = Path(__file__).resolve().parent
FIXTURES_DIR = BASE_DIR / "fixtures"
QUESTIONS_FIXTURE = FIXTURES_DIR / "questions.json"


@shuffle
def get_questions(fixture: Path = QUESTIONS_FIXTURE) -> list[Question]:
    question_instances = []

    with open(fixture, "r", encoding="utf-8") as questions_:
        data = json.load(questions_)

        for obj in data:
            question_instances.append(
                Question(
                    text=obj["q"],
                    difficulty=int(obj["d"]),
                    answer=obj["a"],
                )
            )
    return question_instances


class Question:
    def __init__(self, text: str, difficulty: int, answer: str) -> None:
        self._text = text
        self._difficulty = difficulty
        self._answer = answer.lower()
        self._asked: bool = False
        self.user_answer: [Optional[str]] = None
        self._points: int = 0
        self.possible_points: int = 10 * self._difficulty

    # def __call__(self, **kwargs):
    #     kwargs = {
    #         f"_{key}": value
    #         for key, value in kwargs.items()
    #         if f"_{key}" in self.__dict__
    #     }
    #     self.__dict__.update(kwargs)

    @property
    def points(self) -> int:
        return self._points * self._difficulty

    @property
    def correct(self) -> bool:
        self._asked = True

        if result := self.user_answer.strip().lower() == self._answer:
            if not self._points:
                self._points += 10

        return result

    def __str__(self):
        return f"Вопрос: {self._text}\n" \
               f"Сложность {self._difficulty}/{GRADE}"

    __repr__ = __str__

    @property
    def feedback(self) -> str:
        return (
            f"Ответ неверный, верный ответ {self._answer}\n",
            f"Ответ верный, получено {self.possible_points} баллов\n",
        )[self.correct]  # 0 or 1


if __name__ != "__main__":
    questions: list[Question] = get_questions()

