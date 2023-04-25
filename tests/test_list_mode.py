from main import list_mode


def test_list_mode_1():
    list_1 = []
    for it in list_mode([1, 2, 3, 4, 5, 6, 7, 8], 2):
        list_1.append(it)
    assert list_1 == [2, 4, 6, 8]


def test_list_mode_2():
    list_1 = []
    for it in list_mode([1, 2, 3, 4, 5, 6, 7, 8], 3):
        list_1.append(it)
    assert list_1 == [3, 6]
