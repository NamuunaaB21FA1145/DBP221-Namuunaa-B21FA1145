#!/usr/bin/env python
# coding: utf-8

# In[13]:


def print_stars(n):
    for i in range(1, n + 1):
        print("*" * i)
try:
    n = int(input("Тоо оруул:"))
    print_stars(n)
except ValueError:
    print("Алдаа")


# In[14]:


def print_stars2(n):
    for i in range(1, n + 1):
        print('*' * i)
try:
    n = int(input("Тоо оруул:"))
    print_stars2(n)
except ValueError:
    print("Алдаа")


# In[15]:


students = {
    'Bat': 18,
    'Oyun': 22,
    'Dulam': 21,
    'Suren': 20
}
def max_min_key(dictionary):
    if len(dictionary) == 0:
        return None, None
    else:
        max_key = max(dictionary, key=dictionary.get)
        min_key = min(dictionary, key=dictionary.get)
        return max_key, min_key
max_key, min_key = max_min_key(students)
print(max_key,min_key)


# In[16]:


import numpy as np
array = np.arange(1, 1001)
a= array[(array % 3 == 0) | (array % 7 == 0)]
sum_a= np.sum(a)
sum_a

