# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

class Segment:
    def __init__(self, point1, point2):
        """
        Инициализация отрезка
        :param point1: координаты первой точки
        :param point2: координаты второй точки
        """
        self.point1 = point1
        self.point2 = point2

    def length(self):
        """
        Длинна отрезка
        :return: длинна с округлением до двух знаков после запятой
        """
        x1, y1 = self.point1
        x2, y2 = self.point2
        lenght = pow(((x2-x1)**2 + (y2-y1)**2), 0.5)
        return round(lenght, 2)

    def x_axis_intersection(self):
        """
        Возвращает True, если отрезок пересекает ось абцисс, иначе False
        :return: True / False
        """
        x1, y1 = self.point1
        x2, y2 = self.point2
        return y1 * y2 <= 0

    def y_axis_intersection(self):
        """
        Возвращает True, если отрезок пересекает ось ординат, иначе False
        :return: True / False
        """
        x1, y1 = self.point1
        x2, y2 = self.point2
        return x1 * x2 <= 0


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
