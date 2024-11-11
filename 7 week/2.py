import time
from functools import wraps

def cache_results(func):
    cache = {}  

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if key in cache:
            print("Результат взят из кэша.")
            return cache[key]
        else:
            start_time = time.time() 
            result = func(*args, **kwargs)
            end_time = time.time() 

            cache[key] = result
            elapsed_time = round(end_time - start_time)
            print(f"Выполнено за {elapsed_time} секунд(ы).")
            return result

    return wrapper
