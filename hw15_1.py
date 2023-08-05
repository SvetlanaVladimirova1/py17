# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации.

import logging
FORMAT = "{levelname} - Дата: {asctime}. {msg}"

logging.basicConfig(format=FORMAT, style="{", filename='log3.log', level=logging.ERROR, encoding="UTF-8")

logger = logging.getLogger(__name__)


def calc_perimeter(width: int, heigth: int) -> float | None:
    try:
        a = (width + heigth) * 2
        return a

    except TypeError:
        logger.error(f'Ошибка вычисления периметра: необходимо вводить число')
        return None


def calc_area(width: int, heigth: int):
    try:
        b = heigth * width
        return b
    except TypeError:
        logger.error(f'Ошибка вычисления площади: необходимо вводить число')
        return None


if __name__ == '__main__':
    print(calc_perimeter(4, 'b'))
    print(calc_area('t', 'r'))

