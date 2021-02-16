'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса,
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__()
для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
'''

class Matrix:
    def __init__(self, *args):
        self.matr = []
        self.height = len(args)
        if len(args):
            self.width = len(args[0])
        else:
            self.width = 0
        for el in args:
            self.matr.append(el)

    def __str__(self):
        result = ''
        for el in self.matr:
            result += ' '.join(map(str, el)) + '\n'
        return result

    def __getitem__(self, i, j=None):
        if not j:
            return self.matr[i]
        else:
            return self.matr[i][j]

    def __call__(self, lst):
        self.matr.append(lst)

    def __add__(self, other):
        if self.height != other.height or self.width != other.width:
            print('Нельзя складывать матрицы с разными параметрами!')
        else:
            result = Matrix()
            for i in range(self.height):
                result([el1 + el2 for el1, el2 in zip(self[i], other[i])])
            return result


matr1 = Matrix([1, 34, 6, 12], [5, 23, 78, 45], [12, 4, 6, -6])
matr2 = Matrix([1, 2, 3, 4], [5, 4, 8, 42], [-7, 4, 6, -6])
matr3 = Matrix([12, 34], [344, 0])
matr4 = Matrix([1, -1], [-1, 0])
print(matr1 + matr2)
print(matr3 + matr2)
print(matr3 + matr4)