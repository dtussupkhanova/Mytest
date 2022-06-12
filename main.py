#Первая задача
'''
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != '-': date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Correct'
                else:
                    return f'Invalid year'
            else:
                return f'Invalid month'
        else:
            return f'Invalid day'

    def __str__(self):
        return f'Текущая дата: {Data.extract(self.day_month_year)}'

today = Data('11 - 06 - 2022')
print(today)
print(Data.valid(11, 6, 2022))
print(today.valid(11, 13, 2022))
print(Data.extract('11 - 6 - 2022'))
print(today.extract('11 - 6 - 2022'))
print(Data.valid(1, 5, 2022))
'''
#Вторая задача
'''
class DivisionByNull:
    def __init__(self, divident, divisor):
        self.divident = divident
        self.divisor = divisor

    @staticmethod
    def divide_by_null(divident, divisor):
        try:
            return (divident / divisor)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(200, 10)
print(DivisionByNull.divide_by_null(150, 0))
print(DivisionByNull.divide_by_null(120, 2))
print(div.divide_by_null(200, 0))
print(div.divide_by_null(200, 20))
'''
#Третья задача
'''
class Typeofdata:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                value = input('Введите числа: ')
                self.my_list.append(value)
                print(f'Текущий список: {self.my_list} \n ')
            except:
                print(f'Недопустимое значение')
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Работа выполнена'
                else:
                    return f'Работа выполнена'

try_except = Typeofdata(1)
print(try_except.my_input())
'''
