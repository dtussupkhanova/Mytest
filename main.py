#Первая задача
"""
from sys import argv

print((int(argv[1])*int(argv[2]))+int(argv[3]))
"""
#Вторая задача
'''
li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_li = [j for i,j in zip(li, li[1:]) if j > i]
print(new_li)
'''
#Третья задача
'''
n=[el for el in range(20,241) if el%20==0 or el%21==0]
print(n)
'''
#Четвертая задача
'''
lst1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
lst2= [el for el in lst1 if lst1.count(el)==1]
print(lst2)
'''
#Пятая задача
'''
from functools import reduce
def my_func(q,el):
    return q * el
my_li = [el for el in range(100,1001) if el%2==0]
print(reduce(my_func, my_li))
'''
#Шестая задача
'''
from itertools import count, cycle
for elem in count(3):
    print(elem)
    if elem == 10:
        break

i=0
for el in cycle('привет'):
    print(el)
    i += 1
    if i == 18:
        break
'''
#Седьмая задача
'''
from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

x = 0
for f in fact():
    if x < 5:
        print(f)
        x += 1
    else:
        break
'''
