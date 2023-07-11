import json
import os
from abc import ABC, abstractmethod
from typing import Self, Optional

from settings import FIXTURES_ROOT


class BaseModel(ABC):
    """
    Базовый абстрактный класс для представления моделей данных.
    Необходимо переопределние метода get(cls, search_param: Any)
    для поиска необходимого экземпляра по переданному параметру.

    Attributes:
        pk: int - Первичный ключ.
        skills: list[str] - Список строк с навыками.
        instances: Optional[list[Self]] - список с экземлярами модели.
    """

    pk: int
    skills: list[str]
    instances: Optional[list[Self]] = None

    def __new__(cls, *args, **kwargs):
        if cls.instances is None:
            cls.instances = []
        return super().__new__(cls)

    @property
    def __name__(self):
        return "%s" % self.__class__.__name__.lower()

    @property
    def skills_(self) -> str:
        return ", ".join(self.skills)

    @classmethod
    def load_data(cls):
        """
        Метод для загрузки фикстур в атрибуты
        классов соответствующих моделей.
        """

        for *_, fixtures_names in os.walk(FIXTURES_ROOT):
            for fixture in fixtures_names:
                with open(FIXTURES_ROOT / fixture) as file:
                    # Проверка, что имя файла имеет отношение к имени модели.
                    if fixture.split('.')[0][:-1] == cls.__name__.lower():

                        for data in json.load(file):
                            instance = cls()
                            instance.__dict__.update(data)
                            cls.instances.append(instance)

    @classmethod
    @abstractmethod
    def get(cls, search_param):
        return NotImplemented


class Student(BaseModel):
    full_name: str

    def __str__(self):
        return self.full_name

    __repr__ = __str__

    @classmethod
    def get(cls, pk) -> Self:
        if not isinstance(pk, int):
            try:
                pk = int(pk)
            except ValueError:
                return

        for instance in cls.instances:
            if instance.pk == pk:
                return instance


class Profession(BaseModel):
    title: str

    def __str__(self):
        return self.title

    __repr__ = __str__

    @classmethod
    def get(cls, title) -> Self:
        for instance in cls.instances:
            if instance.title.lower() == title.lower():
                return instance


if __name__ != "__main__":
    Student.load_data()
    Profession.load_data()
