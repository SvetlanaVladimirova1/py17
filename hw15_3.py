# Также реализуйте возможность запуска из
# командной строки с передачей параметров.
import argparse
import logging
FORMAT = "{levelname} - Дата: {asctime}. {msg}"

logging.basicConfig(format=FORMAT, style="{", filename='log3.log', level=logging.ERROR, encoding="UTF-8")

logger = logging.getLogger(__name__)


def pars():
    parser = argparse.ArgumentParser(prog='Прямоугольник со сторонами:', description='Вычисление периметра и площади',
                                     epilog='Вычисление периметра и площади')
    parser.add_argument("param", metavar="w h", type=int, nargs=2, help="Введите w h через пробел")
    args = parser.parse_args()
    return f'{calc_perimeter(*args.param)}\n{calc_area(*args.param)}'


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
    print(pars())
