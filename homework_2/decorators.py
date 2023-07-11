from collections.abc import Callable


def printable_view(as_string: bool = True):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs) -> str | dict[str, set[str] | int]:
            result = func(*args, **kwargs)

            print_view = f"Пригодность {result['fit_percent']}%\n" \
                         f"{kwargs['student']} знает {', '.join(result['has'])}\n" \
                         f"{kwargs['student']} не знает {', '.join(result['lacks'])}"

            return print_view if as_string else result

        return wrapper

    return decorator
