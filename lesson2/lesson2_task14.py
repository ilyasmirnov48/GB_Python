# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 50 -> 1, 2, 4, 8, 16, 32


N = int(input('Введите число '))
x = 0
y = 0
while x < N:
    x = 2 ** y
    y += 1
    if x <= N:
        print(x, end=' ')
else:
    x = N