# Вариант 6.
# 2. Дана действительная квадратная матрица порядка N (N — нечетное), 
# все элементы которой различны. Найти наибольший элемент среди 
# стоящих на главной и побочной диагоналях и поменять его местами с 
# элементом, стоящим на пересечении этих диагоналей.
# Для заданий из практической работы №8 для своего варианта.
# Организовать ввод данных (матриц) из файла (имя: ФИО_группа_vvod.txt)
# И вывод результатов в файл (имя: ФИО_группа_vivod.txt)

a=[]
with open("Шапошников_А.Д._ЗИТ23м_vvod.txt",'r') as file:
    line = file.readline()
    while line:
        a.append(list(map(float,line.split())))
        line = file.readline()

n = len(a)

maxList = []
minList = []

if n % 2 == 0:
    exit("Порядок матрицы четный")    
for i in range(n):
    if len(a[i])!=n:
        exit("Матрица не квадратная")    
    maxList.append(a[i][0])
    minList.append(a[0][i])
    
for i in range(n):
    print(a[i])

max = a[0][0]
imax = 0
jmax = 0
i = j = 0
while i < n and j < n:
    if a[i][j]>max:
        max=a[i][j]
        imax=i
        jmax=j
    if a[i][n-1-j]>max:
        max=a[i][n-1-j]
        imax=i
        jmax=n-1-j
    i+=1
    j+=1

print("Максимальный элемент на диагоналях - a["+str(imax)+","+str(jmax)+"] = "+str(max))

tmp=a[imax][jmax]
a[imax][jmax]=a[(n-1)//2][(n-1)//2]
a[(n-1)//2][(n-1)//2]=tmp

for i in range(n):
    print(a[i])

with open("Шапошников_А.Д._ЗИТ23м_vivod.txt",'w+') as file:
    file.write("Максимальный элемент на диагоналях - a["+str(imax)+","+str(jmax)+"] = "+str(max)+'\n')
    for i in range(n):
        file.write(str(a[i])+'\n')