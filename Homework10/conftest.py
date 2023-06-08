import pytest
import time
import datetime


@pytest.fixture(scope="class")
def tests_timing():
    start = datetime.datetime.now()
    print(start.strftime("\n Прогон тестов запустился в %H:%M:%S:%f"))
    yield
    end = datetime.datetime.now()
    print(end.strftime("\n Прогон тестов завершился в %H:%M:%S:%f"))


@pytest.fixture()
def test_time():
    start = time.time()
    yield
    end = time.time()
    print(f"\n Тест выполнялся {end - start}")