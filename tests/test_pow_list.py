from main import sum_list


def test_pow_list_1():
    assert sum_list([1, 2, 3, 4]) == 100


def test_pow_list_2():
    assert sum_list([1.2, 1.3, -1, -2, 3]) == 6.25

