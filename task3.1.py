# Даны три целых числа. Выбрать из них те, которые принадлежат интервалу [1,3]
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if num1 >= 1 and num1 <= 3:
    print("Первое число приналежит интервалу [1,3]")

if num2 >= 1 and num2 <= 3:
    print("Второе число приналежит интервалу [1,3]")

if num3 >= 1 and num3 <= 3:
    print("Третье число приналежит интервалу [1,3]")