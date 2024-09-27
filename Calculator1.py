from typing import Final
#import math
import sys


#матрицы, статистика, гиперболические функции, матрицы
class Calculator:
    # Константы
    PI: Final = 3.14
    E: Final =2.72
    PLUS_INFINITY = sys.float_info.max
    MINUS_INFINITY = -sys.float_info.max



    class BasicMath:
        @staticmethod
        def fact(n):
            if (n == 1 or n == 0):
                return 1
            else:
                return n * Calculator.fact(n - 1)
    class Statistics:


        #Класс сатистики принадлежит Марату
        '''
        @staticmethod
        def median():
            #Это Сашин метод
            sm = []
            count = 0
            while True:
                a = input("Введите числа, для завершения введите end ")
                if a == "end":
                    break
                sm.append(int(a))
                count += 1
            sm.sort()
            if count == 0:
                return None
            if count % 2 == 0:
                return (sm[count // 2 - 1] + sm[count // 2]) / 2
            else:
                return sm[count // 2]





          @staticmethod
        def average():
            # Это Сашин метод
            sm = []
            while True:
                a = input("Введите числа, для завершения введите end")
                if a == "end":
                    break
                sm.append(int(a))
            if len(sm) == 0:
                return None
            return sum(sm) / len(sm)
                '''

        @staticmethod
        def max_num(sm):

            return max(sm)

        @staticmethod
        def variance(sm):
            #тут дисперсия

            if len(sm) == 0:
                return None
            avg = sum(sm) / len(sm)
            return round(sum((x - avg) ** 2 for x in sm) / len(sm),2)

        @staticmethod
        def average_quadratic(sm):

            if len(sm) == 0:
                return None
            return round((sum(x ** 2 for x in sm) / len(sm)) ** 0.5,2)


        @staticmethod
        def standart_deviation(sm):
            return round(Calculator.Statistics.variance(sm)**0.5,2)

        @staticmethod
        def distribution_mode(sm):

            if len(sm) == 0:
                return None
            freq = {}
            for num in sm:
                freq[num] = freq.get(num, 0) + 1
            mode = max(freq, key=freq.get)
            return mode




# Класс матриц принадлежит Ване
    class Matrix:

        def __init__(self, rows, columns):
            self.rows = rows
            self.columns = columns
            self.data = [[0] * columns for _ in range(rows)]  # Инициализация матрицы нулями

        def set_value(self, row, col, value):
            if row >= self.rows or col >= self.columns:
                raise IndexError("Индекс вышел за границы")
            self.data[row][col] = value

        def get_rows(self):
            return self.rows

        def get_columns(self):
            return self.columns

        def get_value(self, row, col):
            if row >= self.rows or col >= self.columns:
                raise IndexError("Индекс вышел за границы")
            return self.data[row][col]

        @staticmethod
        def addition(self,matrix1,matrix2):
            if matrix1.rows != matrix2.rows or matrix1.columns != matrix2.columns:
                raise ValueError("Размеры матриц должны совпадать")
            matrix3=Calculator.Matrix(matrix1.rows, matrix1.columns)

            for i in range(matrix1.rows):
                for j in range(matrix1.columns):
                    matrix3.set_value(i, j, matrix1.get_value(i, j) + matrix2.get_value(i, j))
            return matrix3

        @staticmethod
        def subtraction(self, matrix1, matrix2):
            matrix3 = Calculator.Matrix(matrix1.rows, matrix1.columns)
            for i in range(matrix1.rows):
                for j in range(matrix1.columns):
                    matrix3.set_value(i, j, matrix1.get_value(i, j) - matrix2.get_value(i, j))
            return matrix3



        @staticmethod
        def multiplication(self, matrix1, matrix2):
            # Проверка на корректность размеров матриц
            if matrix1.columns != matrix2.rows:
                raise ValueError("Число столбцов первой матрицы должно быть равно числу строк второй матрицы")

            matrix3 = Calculator.Matrix(matrix1.rows, matrix2.columns)

            # Умножение матриц
            for row in range(matrix1.rows):
                for j in range(matrix2.columns):
                    sum_value = 0
                    for k in range(matrix1.columns):
                        sum_value += matrix1.get_value(row, k) * matrix2.get_value(k, j)
                    matrix3.set_value(row, j, sum_value)

            return matrix3

        @staticmethod
        def kronecker_multiplication(matrix1, matrix2):
            result_rows = matrix1.rows * matrix2.rows
            result_columns = matrix1.columns * matrix2.columns
            matrix3 = Calculator.Matrix(result_rows, result_columns)

            for i in range(matrix1.rows):
                for j in range(matrix1.columns):
                    for k in range(matrix2.rows):
                        for l in range(matrix2.columns):
                            matrix3.set_value(i * matrix2.rows + k, j * matrix2.columns + l,matrix1.get_value(i, j) * matrix2.get_value(k, l))
            return matrix3

        @staticmethod
        def determinant(matrix1):



            a = matrix1.get_value(0, 0) * (matrix1.get_value(1, 1) * matrix1.get_value(2, 2) - matrix1.get_value(1, 2) * matrix1.get_value(2, 1))
            b = matrix1.get_value(0, 1) * (matrix1.get_value(1, 0) * matrix1.get_value(2, 2) - matrix1.get_value(1, 2) * matrix1.get_value(2, 0))
            c = matrix1.get_value(0, 2) * (matrix1.get_value(1, 0) * matrix1.get_value(2, 1) - matrix1.get_value(1, 1) * matrix1.get_value(2, 0))
            return a - b + c










