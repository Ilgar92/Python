#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np


# In[29]:


a = np.array([[ 1,  6],
       [ 2,  8],
       [ 3, 11],
       [ 3, 10],
       [ 1,  7]])
a


# In[31]:


np.mean(a, axis=0)
mean_a = np.mean(a, axis=0)


# In[32]:


print(mean_a)


# ### Задание 2. 
# Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков, содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.

# In[33]:


a_centered = a - mean_a
print(a_centered)


# ### Задание 3
# Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1, где N - число наблюдений.
# 

# In[44]:


a_centered_sp = a_centered.T[0] @ a_centered.T[1]
print(a_centered_sp)


# In[45]:


a_centered_sp / (a_centered.shape[0] - 1)


# ### Тема “Работа с данными в Pandas”
# Задание 1
# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
# [1, 1, 1, 2, 2, 3, 3],
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].
# 

# In[4]:


import pandas as pd
import numpy as np


# In[7]:


authors = pd.DataFrame({'author_id':[1, 2, 3], 
                       'author_name':['Тургенев', 'Чехов','Островский']}, columns=['author_id', 'author_name'])


# In[9]:


authors


# In[10]:


book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3], 
                    'book_title':['Отцы и дети', 'Рудин','Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                    'price':[450, 300, 350, 500, 450, 370, 290]}, columns=['author_id', 'book_title', 'price'])


# In[12]:


book


# ### Задание 2
# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

# In[17]:


authors_price = pd.merge(authors, book, on = 'author_id', how = 'outer')
authors_price


# ### Задание 3
# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

# In[21]:


top5 = authors_price.nlargest(5, 'price')
top5


# ### Задание 4
# Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

# In[35]:


authors_stat = authors_price.groupby('author_name').agg(min_price=('price', 'min'), 
                                                    max_price=('price', 'max'),
                                                    mean_price=('price','mean'))
authors_stat

