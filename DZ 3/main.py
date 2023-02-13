import numpy


def count_of_x(n: int, x: int):
    print("Задание 1:")
    array: [int] = numpy.random.randint(9, size=n)
    print(array)
    print(str((array == x).sum()))


def find_nearest(n: int, x: float):
    print("Задание 2:")
    array: [int] = numpy.random.randint(9, size=n)
    print(array)
    print(str(min(array, key=lambda y: abs(y - x))))


scores = {
    1: "AEIOULNSTRАВЕИНОРСТ",
    2: "DGKVДКЛМПУ",
    3: "BCMPБГЁЬЯ",
    4: "FHVWYЙЫ",
    5: "KЖЗХЦЧ",
    8: "JXШЭЮ",
    10: "QZФЩЪ"
}


def scrabble(word: str):
    print("Задание 3:", end=" ")
    word = word.upper()
    result: int = 0
    for char in word:
        if scores[1].__contains__(char):
            result += 1
        if scores[2].__contains__(char):
            result += 2
        if scores[3].__contains__(char):
            result += 3
        if scores[4].__contains__(char):
            result += 4
        if scores[5].__contains__(char):
            result += 5
        if scores[8].__contains__(char):
            result += 8
        if scores[10].__contains__(char):
            result += 10
    print(result)


count_of_x(5, 3)
find_nearest(5, 2.6)
scrabble("ноутбук")

