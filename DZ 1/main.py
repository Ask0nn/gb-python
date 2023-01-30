def sum(str):
    result = 0
    for n in str:
        result += int(n)
    return result


def getKatya(petya, sereja):
    print((petya + sereja) + (petya + sereja) * 2)


def isLuckyTicket(ticket):
    if sum(ticket[0:3]) == sum(ticket[3:6]):
        return True
    else:
        return False

# Тут не уверен можно ли не ломать. Так что сделал проверку на количество долек
def checkChocolateBar(n, m, k):
    if k % n == 0 and k != (n * m):
        return True
    else:
        if k % m == 0 and k != (n * m):
            return True
    return False


# print(sum(123))
# getKatya(1, 1)
# print(isLuckyTicket(str(385916)))
print(checkChocolateBar(3, 2, 6))
