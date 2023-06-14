# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.usefixtures("tests_timing")
class Test1:

    @pytest.mark.usefixtures("test_time")
    def test_positive_1(self):
        assert all_division(5, 2) == 2.5

    @pytest.mark.usefixtures("test_time")
    def test_positive_2(self):
        assert all_division(-6, 2) == -3
