#Первая задача

x = 'flag'
print(x)
y = 6
print(y)
z = True
print(z)
w = 5.7
print(w)
c = int(input('Введите целое число: '))
print(a)
d = input('Введите слово: ')
print(b)



#Вторая задача
time = int(input())
hours = time//3600
minutes = (time%3600)//60
seconds = (time%3600)%60

if hours < 10:
    str_hours = '0' + str(hours)
else:
    str_hours = str(hours)

if minutes < 10:
    str_minutes = '0' + str(minutes)
else:
    str_minutes = str(minutes)

if seconds < 10:
    str_seconds = '0' + str(seconds)
else:
    str_seconds = str(seconds)
print(f'{str_hours}:{str_minutes}:{str_seconds}')



#Третья задача
n = input('Введите число: ')
sum = int(n)+int(n*2)+int(n*3)
print(sum)


#Четвертая задача

num = int(input())
i = 0
max_value = 0

arr_of_numbers = [int(x) for x in str(num)]

while i<len(str(num)):
    if arr_of_numbers[i] > max_value:
        max_value = arr_of_numbers[i]
    i += 1

print(max_value)


#Пятая задача

revenue = int(input('Ваша выручка: '))
expenses = int(input('Ваши издержки: '))
if revenue>expenses:
    print('Прибыль')
elif revenue==expenses:
    print('Точка безубыточности')
else:
    print('Убыток')


#Шестая задача

revenue = int(input('Ваша выручка: '))
expenses = int(input('Ваши издержки: '))
if revenue>expenses:
    print(f'Рентабельность:{(revenue-expenses)/revenue}')
    employees = int(input('Введите количество сотрудников: '))
    print(f'Прибыль в расчете на одного сотрудника:{(revenue-expenses)/employees}')
else:
    print('Не прибыльно')


#Седьмая задача
a = int(input('Пробежал км в первый день: '))
b = int(input('Желаемый результат: '))

day = 1
while a<b:
    a = a + 0.1*a
    day += 1
print(day)



