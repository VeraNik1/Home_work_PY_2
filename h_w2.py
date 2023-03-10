# Домашнее задание Семинар 2

# Задача 10 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2


import random as r
while True:
    try:
        n = int(input('Введите количество монет: '))
        if n <= 0:
            raise Exception
        coins = [r.randrange(0, 2) for i in range(n)]
        print('выпали такие монетки:', *coins)
        print(f'минимальное количество монет, которое нужно перевернуть: {min(coins.count(1), coins.count(0))}')
        break
    except:
        print("Вы ввели некорректное значение, попробуйте еще раз")




# Задача 12 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
#  Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.



while True:
    try:
        S = int(input('Введите сумму натуральных чисел X и Y: '))
        P = int(input('Введите произведение натуральных чисел X и Y: '))

        if P <= 0 or S <= 0:
            raise Exception
        x = 0
        y = 0
        for i in range(1, P//2 + 1):
            if P == (S - i) * i:
                x = i
                y = S - i
                break
                
        if x:
            print(f'Петя загадал X = {x} Y = {y}')
        else:
            print('Петя не умеет считать!')
        break
    except:
        print("Вы ввели некорректное значение суммы или произведения, попробуйте еще раз")


# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

while True:
    try:
        N = int(input('Введите натуральное число: '))
        if N <= 0:
             raise Exception
        start = 1 #значение 2 в 0 степени вроде бы целое число)
        while start <= N:
            print(start, end = ' ')
            start *= 2 
        break
    except:
        print("Вы ввели некорректное значение, попробуйте еще раз")       