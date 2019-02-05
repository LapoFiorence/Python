#Easy
#Задача_1
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
import random
a = [-1, 35, 8, -4, 0, 12, -2]
result = [i**2 for i in a ]
print(result)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_a = ['яблоко', 'банан', 'сливы', 'манго', 'виноград']
list_b = ['клубника', 'арбуз', 'манго', 'яблоко', 'апельсины']
result = list (set (list_a) & set (list_b))
print(result)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

a = [0, 5, 9, 33, 18, 12, -9]
result = [el for el in a if el % 3 == 0 and el >=0 and el % 4 !=0]
print(result)

#Normal
# Задача - 1
# Запросите у пользователя имя, фамилию, email.
# Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате:
# текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст,
# допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net),
# te_4_st@test.com - верно указан.
#import re
#name = input('Введите имя: ')
#surname = input('Введите фамилию: ')
#email = input('Укажите e-mail: ')
#pattern_name = '([A-Z_a-z]+)'
#result_name = (re.match(pattern_name, name))
#print(result_name)