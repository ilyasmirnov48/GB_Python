import logging
import argparse
from datetime import datetime


logging.basicConfig(filename='rec.log.', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('<прямоугольник>')


class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_vaue = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        logger.critical(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Свойство {self.param_name} нельзя удалять")
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            logger.critical(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} "
                            f"Значение {value} должно быть целым числом")
            raise TypeError(f'Значение {value} должно быть целым числом')
        if value <= 0:
            logger.critical(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} "
                            f"Физическая величина должна быть больше 0")
            raise ValueError('Физическая величина должна быть больше 0')


class Rectangle:
    width = Range()
    height = Range()

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Находим периметр прямоугольника")
        return 2 * (self.width + self.height)

    def area(self):
        logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Находим периметр прямоугольника")
        return self.width * self.height

    def __add__(self, other) -> int:
        logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Складываем прямоугольники")
        all_perimeter = self.perimeter() + other.perimeter()
        width = int(self.width + other.width)
        height = int(all_perimeter/2 - width)
        return Rectangle(width, height)

    def __sub__(self, other) -> int:
        logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Находим разность прямоугольников")
        new_perimeter = self.perimeter() - other.perimeter()
        if new_perimeter < 0:
            self, other = other, self
            new_perimeter = - new_perimeter
        width = int(abs(self.width - other.width))
        height = int(abs(new_perimeter/2 - width))
        return Rectangle(width, height)

    def __str__(self):
        logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} "
                    f"Получаем следующий результат {self.width} и {self.height}")
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __eq__(self, other):
        logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Сравниваем прямоугольники")
        if self.area() == other.area():
            return True
        else:
            return False

r1 = Rectangle(6, 2)
r2 = Rectangle(3, 3)
print(r1.area())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Площадь прямоугольника')
    parser.add_argument('width', metavar='width', type=int, nargs=1,
                        help='finding the area of a rectangle')
    parser.add_argument('height', metavar='height', type=int, nargs=1,
                        help='finding the area of a rectangle')
    args = parser.parse_args()
    print(Rectangle(args.width, args.height))



