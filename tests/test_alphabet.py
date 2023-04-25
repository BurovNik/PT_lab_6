from main import alphabet


def test_alphabet_1():
    list_1 = []
    for it in alphabet():
        list_1.append(it)
    assert list_1 == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']


def test_alphabet_2():
    list_1 = []
    list_1.append(next(alphabet()))
    assert list_1 == ['a']
