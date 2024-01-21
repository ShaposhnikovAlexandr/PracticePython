# Вариант 6

import math

x = float(input('Введите x: ')) #0.01655
y = float(input('Введите y: ')) #-2.75
z = float(input('Введите z: ')) #0.15

s = math.sqrt(10*(x**(1/3)+x**(y+2)))*(math.asin(z)**2-abs(x-y))
print("s = {0:.2f}".format(s))