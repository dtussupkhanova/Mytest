#Первая задача
'''
li = ['house', 3, True, 5.3, 'cinema', 9, 4.8, 'car', 4, 8.9]
for el in li:
    print(type(el))
'''
#Вторая задача
'''
li = []
number_of_elements = int(input("Из скольки элементов должен состоять список?"))
for element in range(number_of_elements):
    li.append(input('Введите элемент списка: '))

for i in range(0,len(li)-1,2):
        a = li[i]
        li[i] = li[i + 1]
        li[i + 1] = a

print(li)
'''
'''
#Третья задача (вариант со списком)
month = int(input('Введите месяц: '))
seasons = ['зима', 'весна', 'лето', 'осень']

if month in [12,1,2]:
    print(seasons[0])
elif month in [3,4,5]:
    print(seasons[1])
elif month in [6,7,8]:
    print(seasons[2])
else:
    print(seasons[3])
'''
'''
#Третья задача (вариант со словарем)
seasons = {'зима':[12,1,2], 'весна': [3,4,5], 'лето': [6,7,8], 'осень': [9,10,11]}
month = int(input('Введите месяц: '))
for el in seasons:
    if month in seasons[el]:
        print(el)
        break
'''
"""
#Четвертая задача
b = input('Заполните строку:')
my_list = b.split()
for i, elem in enumerate(my_list, 1):
  print(i, elem[:10])
"""
'''
#Пятая задача
my_list = [7, 5, 3, 3, 2]
print(my_list)
while True:
  a = int(input('Введите следующее значение: '))
  my_list.append(a)
  my_list.sort(reverse=True)
  print(my_list)
'''

