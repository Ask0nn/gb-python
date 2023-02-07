# Довольно странное задание и может я что-то не так понял,
# но если число для поиска равно или меньше длины массива,
# то количество вхождений этого числа всегда будет 1.
# Я конечно сделаю чтоб работало, но может вы имели в виду рандомно заполненный массив
def count_of_x(n: int, x: int):
    print("Задание 1:", end=" ")
    array: [int] = range(n)
    print(str(array.count(x)))


# Иии опять та же история вы пишите A[1..N], массив от 1 до n и в примере у вас ответ 6 Вопрос как если пользователь
# вводит длину массива от 1 до 5 и вы сами пишите 1 2 3 4 5, то как ответ 6 ? Ближе всех будет 4 как бы, но может я
# что-то не понимаю в задании. Формулировки заданий довольно сложные для понимания.
def find_nearest(n: int, x: float):
    print("Задание 2:", end=" ")
    array: [int] = range(n)
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

