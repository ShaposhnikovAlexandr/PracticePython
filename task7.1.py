# Вариант 6.
# 1. Составить программу нахождения наибольшего общего делителя (НОД) и 
# наименьшего общего кратного (НОК) двух натуральных чисел НОК(А, В) = 
# (A*B)/НОД(A,B). Использовать подпрограмму алгоритма Евклида для 
# определения НОД.

# НОД Евклида
def GCD(a,b):
    if (a==b):
        return a
    if a>b:        
        return b if a%b==0 else GCD(a-b,b)
    if a<b:
        return a if b%a==0 else GCD(a,b-a)
    
# НОК
def LCM(a,b):
    return a*b/GCD(a,b)

a = int(input("Введите a: "))
b = int(input("Введите b: "))
print("НОД("+str(a)+","+str(b)+")="+str(GCD(a,b)))
print("НОК("+str(a)+","+str(b)+")="+str(int(LCM(a,b))))