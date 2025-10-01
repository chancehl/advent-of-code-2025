import time
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def timed(func: Callable[..., T]) -> Callable[..., tuple[T, float]]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> tuple[T, float]:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result, (end - start) * 1000

    return wrapper
