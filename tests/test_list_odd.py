from main import list_odd


def test_list_odd_1():
    list_1 = []
    for it in list_odd([1, 2, 3, 4, 5, 6, 7, 8]):
        list_1.append(it)
    assert list_1 == [2, 4, 6, 8]


def test_list_odd_2():
    list_1 = []
    for it in list_odd([-1, 3, 2, 5, 4, 9, 5, 6]):
        list_1.append(it)
    assert list_1 == [2, 4, 6]
