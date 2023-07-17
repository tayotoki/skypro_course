from dataclasses import dataclass


@dataclass
class BasicWord:
    word: str
    subwords: list[str]  # noqa

    def is_correct(self, word: str) -> bool:
        return word in self.subwords

    def __len__(self):
        return len(self.subwords) + 1

    def __unicode__(self):
        return self.word.upper()

    __repr__ = __str__ = __unicode__
