# part 1
# task 1

def pow_list_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper


@pow_list_result
def sum_list(list1: list) -> float:
        sum = 0
        for it in list1:
           sum += it
        return sum


print(sum_list([1, 2, 3]))

# task 6


def fahrenheit(func):
    def wrapper(t_c: float) -> float:
        return func(t_c) * 9. / 5. + 32
    return wrapper


@fahrenheit
def temperature_celsius(t_c: float) -> float:
    return t_c


print(temperature_celsius(0))

# task 9


import time


def time_run(func):
    def wrapper(*args, **kwargs) -> float:
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        return end_time - start_time
    return wrapper


@time_run
def algebraic_sum(n: int, k=2) -> int:
    sum_t = 0
    for it in range(n):
        sum_t += it ** k
    return sum_t


print(algebraic_sum(10000000, 2))


# part 2
# task 6


def alphabet():
    n = 0
    while n < 26:
        yield chr(97 + n)
        n += 1


for it in alphabet():
    print(it, end=' ')


# task 10
print('--------------------')


def list_mode(list_1: list, k: int):
    for it in list_1:
        if it % k == 0:
            yield it


for it in list_mode([1, 2, 3, 4, 5, 6, 7, 8], 2):
    print(it, end=' ')

# task 11


def list_odd(list_1: list):
    for it in list_1:
        if it % 2 == 0:
            yield it


for it in list_odd([1, 2, 3, 4, 5, 6, 7, 8]):
    print(it, end=' ')
