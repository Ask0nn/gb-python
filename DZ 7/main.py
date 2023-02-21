import numpy

vowels: [chr] = {'а', 'я', 'у', 'ю', 'и', 'ы', 'э', 'е', 'о', 'ё'}


def winnie_the_pooh(line: str):
    if line.__len__() <= 0:
        return False
    words: [str] = line.split(" ")
    count: int = -1
    for word in words:
        count_of_vowels: int = 0
        for char in word:
            if char in vowels:
                count_of_vowels += 1
        if count < 0:
            count = count_of_vowels
        if count_of_vowels > count or count_of_vowels < count:
            return False
    return True


def print_operation_table(operation, num_rows=9, num_columns=9):
    print('\n'.join(['\t'.join([str(operation(i, j))
                                for j in range(1, num_columns + 1)])
                     for i in range(1, num_rows + 1)]))


print("Задание 1:", end=" ")
if winnie_the_pooh("пара-ра-рам рам-пам-папам па-ра-па-дам"):
    print("Парам пам-пам")
else:
    print("Пам парам")

print("Задание 2:")
print_operation_table(lambda x, y: x * y)

