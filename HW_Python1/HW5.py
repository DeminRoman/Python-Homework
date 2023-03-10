# Задача 26
# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

import os
os.system("cls")


def power(A, B):
    if (B == 1):
        return (A)
    if (B != 1):
        return (A * power(A, B - 1))


A = int(input("Введите число A: "))
B = int(input("Введите его степень B: "))
print("Результат возведения в степень равен:", power(A, B))


# Задача 28
# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только + 1 и - 1.
# Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    else:
        if b > 0:
            return sum(a + 1, b - 1)
        else:
            return sum(a - 1, b + 1)


print(sum(int(input()), int(input())))
