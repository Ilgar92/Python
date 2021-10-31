'Решение задач по уроку 3'

"""
Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. 
Использовать функцию type() для проверки типа. 
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

int1 = 7
float1 = 3.5
str1 = 'Hello'
list1 = ['a', '5']
tuple1 = ('b', '10')
dict1 = {'name': 'Ilgar', 'surname': 'Gurbanov'}

full_list = [int1, float1, str1, list1, tuple1, dict1]
for i in full_list:
    print(f'{i} is {type(i)}')
    


"""
Для списка реализовать обмен значений соседних элементов. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
При нечётном количестве элементов последний сохранить на своём месте. 
Для заполнения списка элементов нужно использовать функцию input().
"""


el_sum = int(input("Введите количество элементов списка: "))
list1 = []
i = 0
el = 0
while i < el_sum:
    list1.append(input("Введите следующее значение списка: "))
    i += 1

for elem in range(int(len(list1)/2)):
       list1[el], list1[el + 1] = list1[el + 1], list1[el]
       el += 2
print(list1) 


"""Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и dict.
"""


seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input('Введите месяц в виде числа:'))
if month == 12 or month == 1 or month ==2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")
        

'''
Пользователь вводит строку из нескольких слов, разделённых
пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное,
выводить только первые 10 букв в слове.
'''

str1 = input("Введите строку:")
word1 = []
num = 1
for el in range(str1.count(' ') + 1):
    word1 = str1.split()
    if len(str(word1)) <= 10:
        print(f" {num} {word1 [el]}")
        num += 1
    else:
        print(f" {num} {word1 [el] [0:10]}")
        num += 1
        
        
'''
Реализовать структуру «Рейтинг», представляющую собой
не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться
после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, 
например, my_list = [7, 5, 3, 3, 2].
'''

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (111 - выход) "))
while digit != 111:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число "))

















