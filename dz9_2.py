'''Задача2.Замедление кода
 В программировании иногда возникает ситуация, когда работу функции нужно
 замедлить.
 Типичный пример — функция, которая постоянно проверяет,
 изменились ли данные на веб-странице или её код.
 Реализуйте декоратор, который перед выполнением декорируемой функции
 ждёт несколько секунд'''

from typing import Callable
import  time
from functools import wraps
import datetime

def slowing_down(seconds):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """ Функция-обертка,которая выполняет замедление на seconds-секунд вызов декорируемой функции"""
            print(f' старт {func.__name__} в {datetime.datetime.now().strftime('%H:%M:%S')}')
            time.sleep(seconds)
            result = func(*args, **kwargs)
            print(f'Peзультат функции {func.__name__} : {result} в {datetime.datetime.now().strftime('%H:%M:%S')}')
            return result
        return wrapper
    return decorator

@slowing_down(10)
def test_func() -> None:
    """Проверка декоратора и вывод простого сообщения"""

    print('<Тут что-то происходит...>')


if __name__ == '__main__':
    test_func()



