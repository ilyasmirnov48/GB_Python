# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# РРРОРООРОРР -> 4
# ОРОРОРОРОРО -> 5

n = int(input('Введите количество монет '))
orel = 0
reshka = 0
for i in range(n):
    x = int(input('Если монета лежит вверх гербом, введите (1), если решкой (0): '))
    if x == 1:
        orel += 1
    elif x == 0:
        reshka += 1
    else:
        print('Недопустимое значение!')
if orel < reshka:
    print(f'Переверните {orel} монет с орла на решку, их меньше всего')
elif orel == reshka:
    print(f'Количество орлов и решек одинаково, по {orel} штук')
else:
    print((f'Переверните {reshka} монет с решки на орла, их меньше всего'))  