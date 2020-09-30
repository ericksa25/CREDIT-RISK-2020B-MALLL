import functools
import time


def timeit(logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            out = func(*args, **kwargs)
            logger.warning("Execution time %s" % (time.time() - start))
            return out
        return wrapper
    return decorator


def method_caching(func):
    simple_cache = {}

    @functools.wraps(func)
    def wrapper(self, **kwargs):
        key = hash(frozenset(kwargs.items()))
        if key in simple_cache:
            return simple_cache[key]
        simple_cache[key] = func(self, **kwargs)
        return wrapper(self, **kwargs)
    return wrapper
