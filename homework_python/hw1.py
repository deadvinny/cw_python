# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


# number = int(input('Введите число: '))
# a = number // 100
# b = number % 100 // 10
# c = number % 10
#
# res = a + b + c

# print(res)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# n = int(input('Введите число: '))

# s = n / 6
# p = s
# k = n - (s + p)

# print(int(s), int(k), int(p))


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# n = int(input('Введите число: '))

# sum = n // 100000
# sum = sum + (n % 100000 // 10000)
# sum = sum + (n % 10000 // 1000)
# sum2 = n % 1000 // 100
# sum2 = sum2 +(n % 100 // 10)
# sum2 = sum2 +(n % 10)
# if sum == sum2:
#     print('YES')
# else:
#     print('NO')
# print(int(sum), int(sum2))

# Задача 8: Требуется определить, можно ли от шоколадки размером a
# × b долек отломить c долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# a = 3
# b = 2
# c = 1
#
# if c < (a * b) and c % a == 0 or c % b == 0:
#     print('yes')
# else:
#    print('no')