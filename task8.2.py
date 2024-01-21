# Вариант 6.
# 2. Дана действительная квадратная матрица порядка N (N — нечетное), 
# все элементы которой различны. Найти наибольший элемент среди 
# стоящих на главной и побочной диагоналях и поменять его местами с 
# элементом, стоящим на пересечении этих диагоналей.

n = 3
a = [0]*n
for i in range(n):
    a[i]=[0]*n

print("Ввод массива:")
for i in range(n):
    for j in range(n):
        a[i][j]=float(input(str(i)+":"+str(j)+" = "))
    
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
    print(str(a[i]))