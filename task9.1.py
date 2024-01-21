# Вариант 6.
# 1. Дана целочисленная квадратная матрица. Найти в каждой строке 
# наибольший элемент и в каждом столбце наименьший. Вывести на 
# экран.
# Для заданий из практической работы №8 для своего варианта.
# Организовать ввод данных (матриц) из файла (имя: ФИО_группа_vvod.txt)
# И вывод результатов в файл (имя: ФИО_группа_vivod.txt)

a=[]
with open("Шапошников_А.Д._ЗИТ23м_vvod.txt",'r') as file:
    line = file.readline()
    while line:
        a.append(list(map(int,line.split())))
        line = file.readline()

n = len(a)

maxList = []
minList = []

for i in range(n):
    if len(a[i])!=n:
        exit("Матрица не квадратная")
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

with open("Шапошников_А.Д._ЗИТ23м_vivod.txt",'w+') as file:
    for i in range(len(maxList)):
        file.write("Наибольший элемент в строке "+str(i+1)+": "+str(maxList[i])+'\n')
    for i in range(len(minList)):
        file.write("Наименьший элемент в столбце "+str(i+1)+": "+str(minList[i])+'\n')