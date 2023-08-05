# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации.

import logging
FORMAT = "{levelname} - Дата: {asctime}. {msg}"

logging.basicConfig(format=FORMAT, style="{", filename='log1.log', level=logging.INFO, encoding="UTF-8")

logger = logging.getLogger(__name__)


def calc_perimeter(width: int, heigth: int) -> float:
    a = (width + heigth) * 2
    logger.info(f'Периметр равен {a}')
    return a


def calc_area(width: int, heigth: int):
    b = heigth * width
    logger.info(f'Площадь равна {b}')
    return b


if __name__ == '__main__':
    print(calc_perimeter(5, 5))
    print(calc_area(5, 5))

