# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введи число: "))
count = 1
while count < N:
    print(count)
    count *= 2