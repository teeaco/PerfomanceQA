# Реализуйте декоратор @cache_results, который будет кэшировать результаты функции на основе её аргументов. 
# Если функция вызывается с теми же аргументами повторно, декоратор должен возвращать результат из кэша, а 
# не выполнять функцию снова.

# Требования:

# При первом вызове функции с определенными аргументами, декоратор должен выполнить функцию, сохранить результат в кэше и вывести сообщение Выполнено за {кол-во секунд} секунды.

# При повторном вызове функции с теми же аргументами, декоратор должен вернуть результат из кэша и вывести сообщение Результат взят из кэша. (Функция должна выполниться моментально, здесь замерять время не нужно)

# В этой задаче работаем с функциями, принимающими любое количество аргументов.

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
