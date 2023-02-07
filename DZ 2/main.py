def monetka(str: str):
    sides: [int] = [int(numeric_string) for numeric_string in str.strip().split(" ")]
    return sides.count(0) if sides.count(1) > sides.count(0) else sides.count(1)

def zagadka(x: int, y: int):
    print("Задание 2:")
    if x <= 1000 and y <= 1000:
        print("\ts = " + str(x + y))
        print("\tp = " + str(x * y))
    else:
        print("\tx or y > 1000")

def superPow(n: int):
    print("Задание 3:", end=' ')
    x: int = 0
    if n > 0:
        while True:
            result: int = pow(2, x)
            x += 1
            if result > n:
                break
            else:
                print(str(result), end=' ')
    else:
        print("\tn <= 0")


print("Задание 1: " + str(monetka("1 1 0 0 1 1 1 0 0 0 0 0")))
zagadka(2, 3)
superPow(50)

