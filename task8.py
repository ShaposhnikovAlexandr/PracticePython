# Вариант 6.
# 1. Дана целочисленная квадратная матрица. Найти в каждой строке 
# наибольший элемент и в каждом столбце наименьший. Вывести на 
# экран.
n = 3
a = [0]*n
for i in range(n):
    a[i]=[0]*n

maxList = []
minList = []

print("Ввод массива:")
for i in range(n):
    for j in range(n):
        a[i][j]=int(input(str(i)+":"+str(j)+" = "))
    maxList.append(a[i][0])
    minList.append(a[0][i])
    

for i in range(n):
    print(a[i])

for i in range(n):
    for j in range(n):
        if a[i][j]>maxList[i]:
            maxList[i] = a[i][j]

for i in range(n):
    for j in range(n):
        if a[j][i]<minList[i]:
            minList[i] = a[j][i]

for i in range(len(maxList)):
    print("Наибольший элемент в строке "+str(i+1)+": "+str(maxList[i]))

for i in range(len(minList)):
    print("Наименьший элемент в столбце "+str(i+1)+": "+str(minList[i]))
