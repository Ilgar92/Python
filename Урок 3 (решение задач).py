#Урок 3. Домашнее задание

"""
Реализовать функцию, принимающую два числа (позиционные аргументы) 
и выполняющую их деление. Числа запрашивать у пользователя, 
предусмотреть обработку ситуации деления на ноль.
"""

def div(*args):
    try:
        arg1 = int(input('Введите делимое:'))
        arg2 = int(input('Введите делитель:'))
        res = arg1 / arg2
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return 'Обрати внимание! На ноль делить нельзя!'
    return res

    if arg2 != 0:
        return arg1/arg2
    else:
        print('Неверное число. Деление невозможно')

print(f'result  {div()}')



""" Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, 
город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой. 
"""

def my_func(name, surname, byear, city, email, phone):
    return ' '.join(f'name= Ilgar, surname= Gurbanov, byear= 1992, city= Shamkir, email= i.gurbanov@yahoo.com, phone= 8-903-125-25-77')

my_func(name= 'Ilgar', surname='Gurbanov', byear=1992, city='Shamkir', email='i.gurbanov@yahoo.com', phone='8-903-125-25-77')


""" Реализовать функцию my_func(), которая принимает 
три позиционных аргумента, и возвращает сумму наибольших 
двух аргументов.
"""

def my_func(x, y, z):
    sequence = [x, y, z]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    print(sum(total))
my_func(8, 17, 9)


"""
Программа принимает действительное положительное число x
и целое отрицательное число y. Необходимо выполнить 
возведение числа x в степень y. Задание необходимо 
реализовать в виде функции my_func(x, y). При решении 
задания необходимо обойтись без встроенной функции 
возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, 
предусматривающая использование цикла.
"""

def my_func(x, y):
    return x ** abs(y)
my_func(3, -3)

"""
Программа запрашивает у пользователя строку чисел,
разделенных пробелом. При нажатии Enter должна 
выводиться сумма чисел. Пользователь может продолжить 
ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже 
подсчитанной сумме. Но если вместо числа вводится 
специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, 
то вначале нужно добавить сумму этих чисел к полученной 
ранее сумме и после этого завершить программу.
"""
import sys

result = 0
while True:
    line = input("Enter number or special token q fo exite: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'q':
                print(f"You sum is {result}. Program is terminated")
                exit(0)
            else:
                print(f"You sum is {result}. Input error", file=sys.stderr)
                exit(1)
                
"""Реализовать функцию int_func(), принимающую слово
из маленьких латинских букв и возвращающую его же, 
но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна 
попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы.
Необходимо использовать написанную 
ранее функцию int_func().
"""


def func(a):
        return a.title()
print(func("ilgar gurbanov maisovich"))





























    
