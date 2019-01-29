#Easy
#Задача_1

fruts = ['Яблоко ', 'Банан ', 'Виноград ', 'Сливы ', 'Арбуз ', 'Шпроты ']
for index, value in enumerate(fruts, 1):
    print("{}. {:>9}".format(index, value))

#Задача_2

a = ['Саша', 'Маша', 'Оля', 'Петя', 'Света']
b = ['Маша', 'Катя', 'Зина', 'Петя', 'Егор']
for i, x in enumerate(a):
    for ii, y in enumerate(b):
        if x == y:
            a.pop(i)
    print(a)

#Задача_3

a = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
b = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(a[i] / 4)
    else:
        b.append(a[i] * 2)
print(b)



#Normal
#Задача 1

import math
a = [4, 5, 9, 16, 25, 37]
b = []
for i in a:
    if i > 0:
        ii = math.sqrt(i)
        if ii % int(ii) == 0:
            b.append(ii)
print(b)

#Задача_3

import math
import random
a = []
n = 50
count = 0
while count < 50:
    a.append(random.randint(-100, 100))
    count += 1
print(a)

#Задача_4
a = [1, 2, 2, 4, 8, 5, 4]
b = set(a)
print (b)
c = [x for x in a if not a.count(x) > 1]
print(c)