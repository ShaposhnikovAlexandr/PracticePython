# Вариант 6
# В строке удалить все буквы "а" и подсчитать количество удаленных символов.

string = input("Введите строку: ")
count=0
i = 0
while i in range(len(string)):
    if string[i]=="а":
        string=string[0:i]+string[i+1:len(string)]
        count+=1
    else:
        i+=1

print("Результат: "+string)
print("Количество удалений: "+str(count))