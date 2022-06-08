#Первое задание
'''
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        self.ans = ''
        for i in range(len(self.matrix)):
            self.ans += '\n'
            for j in range(len(self.matrix[i])):
                self.ans = self.ans + str(self.matrix[i][j]) + ' '

        return self.ans

    def __add__(self, other):
        self.ans = ''
        for i in range(len(self.matrix)):
            self.ans += '\n'
            for j in range(len(self.matrix[0])):
                self.ans = self.ans + str(self.matrix[i][j]+other.matrix[i][j]) + ' '

        return self.ans

m = Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(m)

n = Matrix([[9,8,7],[6,5,4],[3,2,1]])

print(m+n)
'''
#Вторая задача
'''
class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def fabric_for_coat(self):
        return self.size / 6.5 + 0.5

    def fabric_for_costume(self):
        return self.height * 2 + 0.3

    @property
    def all_fabric(self):
        return str(f'Обший расход ткани: {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.for_coat = (self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто: {self.for_coat}'


class Costume(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.for_costume = (self.height * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм: {self.for_costume}'

coat = Coat(42, 2)
costume = Costume(44, 3)
print(coat)
print(costume)
print(coat.all_fabric)
print(costume.all_fabric)
'''
#Третья задача
''''''
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return self.quantity * "*"

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно')


    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))


    def make_order(self, quantity_in_row):
        row = ''
        for i in range(int(self.quantity / quantity_in_row)):
            row += f'{"*" * quantity_in_row} \\n'
        row += f'{"*" * (self.quantity % quantity_in_row)}'
        return row

cell1 = Cell(2)
cell2 = Cell(8)
print(cell1)
print(cell2)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell2.make_order(5))
print(cell1.make_order(10))
print(cell1 / cell2)
''