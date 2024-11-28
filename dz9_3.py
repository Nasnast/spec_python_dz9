'''Задача 3. Счётчик
 Реализуйте декоратор counter, считающий и выводящий количество вызовов
 декорируемой функции.
 Для решения задачи нельзя использовать операторы global и nonlocal.
 Пример: Из файла products.json нужно создать products.csv'''

import json
import csv
from typing import Callable
from pathlib import Path
from functools import wraps

def counter(func: Callable):

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count +=1
        print(f'функция {func.__name__} была вызвана {wrapper.count} раз')
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@counter
def json_to_csv(file_name: Path) -> None:
    with open(file_name, encoding='utf-8') as json_file:
        data = json.load(json_file)

    with open(f'{file_name.stem}.csv', 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data[0].keys())
        for row in data:
            csv_writer.writerow(row.values())


if __name__ == '__main__':
    json_to_csv(Path('products.json'))
    json_to_csv(Path('products.json'))
