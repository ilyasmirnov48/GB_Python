# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 7, 10 -> 2, 5 (2 + 5 == 7; 2 * 5 == 10)


S = int(input('Введите сумму двух натуральных чисел '))
P = int(input('Введите произведение тех же двух натуральных чисел '))
D = (S ** 2) - (4 * P)
if D < 0:
    print('Недопустимые значения!')
elif D == 0:
    y = int(S / 2)
    x = int(S - y)
    if x < 1000 or y < 1000:
        print(x, y)
    else:
        print('Недопустимые значения!')
elif D > 0:
    y = abs(int(((-S - (D ** (0.5))) / 2)))
    x = abs(int(((-S + (D ** (0.5))) / 2)))
    if x < 1000 or y < 1000:
        print(x, y)
    else:
        print('Недопустимые значения!')