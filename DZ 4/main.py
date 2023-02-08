import numpy


# Делать input весело конечно, но рандом быстрее. Если вдруг вот вам прям нужен этот input, то переделаю.
def sort_two_arrays(n: int, m: int):
    print("Задание 1:")
    array1: [int] = numpy.random.randint(8, size=n)
    array2: [int] = numpy.random.randint(8, size=m)
    print(array1)
    print(array2)
    result_array: [int] = numpy.intersect1d(array1, array2)
    result_array = numpy.sort(result_array)
    print(result_array)


sort_two_arrays(10, 10)

