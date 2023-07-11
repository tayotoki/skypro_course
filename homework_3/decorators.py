import random as rd
from collections.abc import MutableSequence
from copy import copy


def shuffle(func):
    def wrapper(*args, **kwargs):
        result = copy(func(*args, **kwargs))

        if isinstance(result, MutableSequence):
            rd.shuffle(result)

        return result

    return wrapper
