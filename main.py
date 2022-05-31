#Первая задача
'''
f = open('ex1.txt', 'w', encoding = 'utf-8')
line = input('Введите текст \n')
while True:
    f.writelines(line)
    line = input('Введите текст \n')
f.close()

f = open('ex1.txt', 'r')
a = f.readlines()
print(a)
f.close()
'''
#Вторая задача
'''
my_f = open('ex2.txt', 'r', encoding='utf-8')
counter = 0
num_of_words = 0
data = my_f.read()


ls = data.split("\n")

for i in ls:
    if i != "":
        counter += 1
        num_of_words += len(i.split())

print(f'Количество строк в тексте: {counter}')
print(f'Количество слов в тексте: {num_of_words}')

my_f.close()
'''
#Третья задача
'''
file = open('ex3.txt','r', encoding='utf-8')
salary = file.read()
my_list = salary.split("\n")
without_empty_strings = [string for string in my_list if string != ""]
print(without_empty_strings)
salaries = []
for el in without_empty_strings:
    salaries.append(el.split()[1])
    salaries = [float(x) for x in salaries]
    if float(el.split()[1]) < 20000:
        print(el)

print(f'Средняя зпшка: {round((sum(salaries)/len(salaries)),2)}')
file.close()
'''
#Четвертая задача
'''
rus = {'One' :'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('ex4.txt', 'r') as f:
    for line in f:
        ls = line.split('—')
        ls[0] = rus[ls[0][:-1]]
        new_file.append(ls[0]+ " —" + ls[1])

print(new_file)
with open('ex4.txt','w') as f2:
    f2.writelines(new_file)
'''


#Пятая задача
'''
file = open('ex5.txt','w',encoding='utf-8')
file.write(input('Пожалуйста, введите набор чисел: '))
file.close()

file = open('ex5.txt','r',encoding='utf-8')
data = file.read()
ls = data.split()
ls = [int(x) for x in ls]
print(sum(ls))

file.close()
'''
#Шестая задача
'''
subjects = {}
file = open('ex6.txt','r',encoding='utf-8')
subject = file.read()
my_ls = subject.split()
print(my_ls)
for i in range(0,len(my_ls),4):
    count = 0
    print(my_ls[i])
    if my_ls[i+1].split('(')[0] != '—':
        count += int(my_ls[i+1].split('(')[0])

    if my_ls[i+2].split('(')[0] != '—':
        count += int(my_ls[i+2].split('(')[0])

    if my_ls[i+3].split('(')[0] != '—':
        count += int(my_ls[i+3].split('(')[0])

    subjects[my_ls[i][:-1]] = count

print(subjects)

file.close()
'''

#Седьмая задача
'''
import json
companies = {}
profits = []

with open('ex7.txt', 'r') as f:
    for line in f:
        name, type_of_property, revenue, costs = line.split()
        profit = int(revenue)-int(costs)
        companies[name] = profit
        if profit>0:
            profits.append(profit)


av_profit = round(sum(profits)/len(profits))

ans = [companies,{'average_profit':av_profit}]
print(ans)

with open('ex7.json', 'w', encoding='utf-8') as f_js:
    json.dump(ans, f_js)
'''








