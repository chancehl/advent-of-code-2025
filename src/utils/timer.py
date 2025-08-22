from functools import wraps
import time


def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_ms = (end - start) * 1000
        print(f"{func.__name__} took {elapsed_ms:.3f}ms")
        return result

    return wrapper
