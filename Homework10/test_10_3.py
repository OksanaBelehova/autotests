# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result', [
    pytest.param(5, 0, ZeroDivisionError,  marks=pytest.mark.skip("bad test")),
    pytest.param(7, 2, 3.5),
    pytest.param(8, 2, 4, marks=pytest.mark.smoke),
    pytest.param(-3, 3, -1),
    pytest.param(10, 5, 2),
])
def test_division(a, b, result):
    assert all_division(a, b) == result
