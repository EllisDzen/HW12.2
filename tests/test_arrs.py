from utils import arrs


# В функции test_get(): изменила ожидаемое значение в первом утверждении на 2, так как индексация начинается с 0, а не с 1.
def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


# В функции test_slice(): изменений не потребовалось, так как тесты соответствуют ожиданиям.
def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
