import itertools
import math


def is_prime(n):
    if n < 2:
        return False
    square = int(math.sqrt(n)+1)
    for i in range(2, square):
        if n % i == 0:
            return False
    return True


def primes():
    yield 2
    yield 3
    i = 3
    while True:
        i += 2
        if is_prime(i):
            yield i


def primes1():
    i, f = 2, 1  # число и факториал предыдущего числа
    while True:
        if (f + 1) % i == 0:  # проверяем на простоту по теореме Вильсона через факториал
            yield i
        f, i = f * i, i + 1  # сначала пересчитываем факториал для текущего числа, затем увеличиваем число


def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)


def main():
    print(list(itertools.takewhile(lambda x: x <= 100, primes())))
    print(list(itertools.takewhile(lambda x: x <= 100, primes1())))


main()
