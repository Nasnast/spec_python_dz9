''' Задача 4. Кэширование для ускорения вычислений
 Создайте декоратор, который кэширует (сохраняет для дальнейшего использования)
 результаты вызова функции и, при повторном вызове с теми же аргументами,
 возвращает сохранённый результат.
 Примените его к рекурсивной функции вычисления чисел Фибоначчи.
 В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и,
 если такие аргументы уже использовались, должен вернуть сохранённый результат
 вместо запуска расчёта'''

from typing import Callable
from functools import wraps

def cache(func: Callable):
    """Функция-декоратор выполняет кеширование"""
    cache_dict = {}
    @wraps(func)
    def wrapper(num):
        """ Функция-обертка, которая сначала проверяет кэш перед вызовом функции."""
        if num in cache_dict:
            return cache_dict[num]
        result = func(num)
        cache_dict[num] = result
        print(cache_dict[num])
        return result
    return wrapper

@cache
def fibonacci_recursive(n):
    """ Функция для вычисления чисел Фибоначчи с использованием рекурсии"""
    if n <= 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


if __name__ == '__main__':
    print(fibonacci_recursive(0))
    print(fibonacci_recursive(1))
    print(fibonacci_recursive(10))
    print(fibonacci_recursive(3))
    print(fibonacci_recursive(3))

