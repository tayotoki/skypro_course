from collections.abc import Callable


def printable_view(as_string: bool = True):
    """
    Декоратор для представления данных в виде строки.

    Parameters
    ----------
    as_string : bool - Булево значение, если true -
    итоговые данные представляются в виде строки, иначе -
    словаря.

    Returns
    -------
    Строку или словарь с данными, в зависимости от параметра as_string.
    """
    def decorator(func: Callable):
        def wrapper(*args, **kwargs) -> str | dict[str, set[str] | int]:
            result = func(*args, **kwargs)

            print_view = f"Пригодность {result['fit_percent']}%\n" \
                         f"{kwargs['student']} знает {', '.join(result['has'])}\n" \
                         f"{kwargs['student']} не знает {', '.join(result['lacks'])}"

            return print_view if as_string else result

        return wrapper

    return decorator
