# Напишите класс Trigon, для инициализации передаётся неизвестное кол-во атрибутов

# В классе при инициализации происходит проверка на корректность переданных данных и генерируются следующие исключения:

# 1) Если хотя бы одна сторона передана не числом,
# то падаем с TypeError и текстом 'Стороны должны быть числами'

# 2) Если хотя бы одна сторона передана нулем или отрицательным числом,
# то падаем с ValueError и текстом 'Стороны должны быть положительными'

# 3) Если не соблюдается неравество треугольника,
# то Exception и текст "Не треугольник"

# 4) Если передано не 3 аргумента, то IndexError "Передано {n} аргументов, а ожидается 3", где n - кол-во аргументов

import unittest  # Не удалять

# Здесь пишем код


class Trigon:
    def __init__(self, *args):
        """
        Функция по трем точкам проверяет треугольник ли у нас
        :param args: координаты
        """
        self.args = args
        if len(self.args) != 3:
            raise IndexError(f'Передано {len(self.args)} аргументов, а ожидается 3')
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]
        if not isinstance(self.a, int) or not isinstance(self.b, int) or not isinstance(self.c, int):
            raise TypeError("Стороны должны быть числами")
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError('Стороны должны быть положительными')
        elif not self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b:
            raise Exception('Не треугольник')

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


class MyTestCase(unittest.TestCase):

    def test(self):
        data = [(3, '7', 5), (-3, 7, 5), (2, 5, 2), (3, 4, 5, 6), (3, 4), (3, 4, 5)]

        test_data = [('Стороны должны быть числами', 'TypeError'),
                     ('Стороны должны быть положительными', 'ValueError'),
                     ("Не треугольник", 'Exception'),
                     ("Передано 4 аргументов, а ожидается 3", 'IndexError'),
                     ("Передано 2 аргументов, а ожидается 3", 'IndexError'),
                     0]
        for i, d in enumerate(data):
            try:
                Trigon(*data[i])
            except Exception as e:
                assert e.args[0] == test_data[i][0], 'Исключение имеет неправильный текст'
                assert type(e).__name__ == test_data[i][1], 'У исключения неправильный тип'

        print('Всё ок')


if __name__ == '__main__':
    unittest.main()