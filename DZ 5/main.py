import numpy


def recursion_pow(x: int, n: int):
    if n == 0:
        return 1
    if n >= 1:
        return x * recursion_pow(x, n - 1)


def recursion_sum(x: int, y: int):
    if y == 0:
        return x
    else:
        return 1 + recursion_sum(x, y - 1)


print("Задание 1: " + str(recursion_pow(3, 5)))
print("Задание 2: " + str(recursion_sum(2, 2)))

