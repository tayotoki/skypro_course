from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    used_words: set[str] = field(default_factory=set)

    def __len__(self):
        return len(self.used_words)

    def add(self, word: str):
        self.used_words.add(word)

    def is_used(self, word: str) -> bool:
        return word in self.used_words

    def __unicode__(self):
        return self.name

    __str__ = __repr__ = __unicode__
