from main import temperature_celsius


def test_fahrenheit_1():
    assert temperature_celsius(0) == 32.


def test_fahrenheit_2():
    assert temperature_celsius(12) == 53.6
