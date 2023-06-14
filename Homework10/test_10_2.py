# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


def test_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(2, 0)


@pytest.mark.smoke
def test_positive_1():
    assert all_division(7, 2)


@pytest.mark.smoke
def test_positive_2():
    assert all_division(8, 2)


@pytest.mark.smoke
def test_positive_3():
    assert all_division(-3, 3)


def test_negative():
    with pytest.raises(TypeError):
        assert all_division("7", 5)
