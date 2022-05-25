#Первая задача
'''
def my_funct(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Don't divide by zero"
print(my_func(9,1))
'''
#Вторая задача
'''
def user(name, surname, date, city, email, phone):
    print(f'Surname: {surname}, Name: {name}, Date of birth: {date}. Lives in {city}. Contact details: {email}, {phone}')

user(surname="Tussupkhanova", name="Diana", date="12.05.1995", city='Almaty',email='dianaa@gl.com', phone="88005553535")
'''
#Третья задача
"""
def my_func(a, b, c):
    li1 = [a,b,c]
    max1 = max(li1)
    li1.remove(max1)
    max2 = max(li1)
    return max1+max2

print(my_func(8,5,3))
"""
#Четвертая задача (первый вариант)
'''
def my_func(x, y):
    return x**y
print(my_func(2,-2))
'''
#Четвертая задача (второй вариант)
'''
def my_func(x,y):
    ans = 1/x
    y = abs(y)-1
    while y!=0:
        ans = ans*1/x
        y -= 1
    return ans

print(my_func(3,-3))
'''
#Пятая задача
'''
def my_str():
    summ = 0
    full_list = []
    while True:

        str = input('Введите числа: ')
        ls = str.split()
        for el in ls:
            if el == 'stop':
                ls = ls[:ls.index(el)]
                ls = [int(x) for x in ls]
                full_list += ls     #[1,45,6]+[5,7] = [1,45,6,5,7]
                print(full_list)
                summ += sum(ls)
                print(summ)
                return

        ls = [int(x) for x in ls]
        full_list += ls
        print(full_list)
        summ += sum(ls)
        print(summ)
        
my_str()
'''
#Шестая задача
'''
def int_func():
    b = input('Введите слова: ')
    return b.capitalize()

print(int_func())
'''

#Седьмая задачи
'''
def int_func():
    b = input('Введите текст: ')
    return b.title()

print(int_func())
'''



