#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:23:26 2021

@author: IlgarGurbanov
"""

s = 'file.zip'

if s[-3:] == 'zip'
print('!zip')

s = '0123456789'
print(s[4:7])
print(s[1:7:2])
print(s[::-1])
print(s[1:7:2])


v = [x for x in range (0, 100, 10)]


s = 'text.file.zip'
s.split



v0 = [x for x in range(5)]
v1 = [x for x in range(3, 8)]
list( set(v0) & set(v1) )
list( set(v0) | set(v1) )
list( set(v0) ^ set(v1) )
list( set(v0) - set(v1) )

st = set(v0)
st = list(set(v))



keys = ['k' + str(x) for x in range(5)]
values = [x/3.3 for x in range(0, 15, 3)]
dct1 = dict(zip(keys, values))


for key in dct1.keys():
    print(key, dct1[key])
    
    
    
    original_password = 'x777' # правильный пароль, хранится в программе
password = input('Введите пароль: ')  # просим пользователя ввести пароль
access = False  # переменная, хранит разрешение на доступ
if password == original_password: # если введен правильный пароль
    print('Пароль принят, добро пожаловать в систему')
    access = True
if password != original_password: # если введен неправильный пароль
    print('Пароль неверен, вход запрещен')
    
    
    
    
    original_password = 'x777' # правильный пароль, хранится в программе
password = input('Введите пароль: ') # просим пользователя ввести пароль
access = False # переменная, хранит разрешение на доступ
# Если введен правильный пароль
if password == original_password:
    print('Пароль принят, добро пожаловать в систему')
    access = True
# Иначе, т.е. если неправильный пароль
else:
    print('Пароль неверен, вход запрещен')
    
    
    
    color = 'red'
if color == 'blue':
    print('синий')
# elif сокращение от else if(иначе если)
elif color == 'red': 
    print('красный')
elif color == 'green':
    print('зеленый')
# else выполняется, только если все предыдущие проверки вернули False
else:       	
    print('неизвестный цвет')
    
    
numb_1 = int(input("Введите первое целое число: "))
numb_2 = int(input("Введите второе целое число: "))

if numb_1 != numb_2:
    print("Числа не равны")
    if numb_1 > numb_2:
        print("Первое число больше второго")
    elif numb_1 < numb_2:
        print("Первое число меньше второго")
elif numb_1 == numb_2:
    print("Числа равны")
    
    