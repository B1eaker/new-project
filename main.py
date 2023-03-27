def summ(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n //= 10
    print('Сумма цифр равна: ', summ)
    return summ


def count(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    print('Количество цифр в числе: ', count)
    return count


n = int(input('Введите целое положительное число: '))
summ = summ(n)
count = count(n)

print('Разность суммы и количества цифр:', summ - count)
