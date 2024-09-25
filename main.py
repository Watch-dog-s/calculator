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

    @staticmethod
    def fact(n):
        if (n == 1 or n == 0):
            return 1
        else:
            return n * Calculator.fact(n - 1)

    class Statistics:
        @staticmethod
        def median():
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
        def variance():
            #тут дисперсия
            sm = []
            while True:
                a = input("Введите числа, для завершения введите end ")
                if a == "end":
                    break
                sm.append(int(a))
            if len(sm) == 0:
                return None
            avg = sum(sm) / len(sm)
            return sum((x - avg) ** 2 for x in sm) / len(sm)

        @staticmethod
        def average_quadratic():
            sm = []
            while True:
                a = input("Введите числа, для завершения введите end ")
                if a == "end":
                    break
                sm.append(int(a))
            if len(sm) == 0:
                return None
            return (sum(x ** 2 for x in sm) / len(sm)) ** 0.5

        @staticmethod
        def distribution_mode():
            sm = []
            while True:
                a = input("Введите числа, для завершения введите end")
                if a == "end":
                    break
                sm.append(int(a))
            if len(sm) == 0:
                return None
            freq = {}
            for num in sm:
                freq[num] = freq.get(num, 0) + 1
            mode = max(freq, key=freq.get)
            return mode

        @staticmethod
        def average():
            sm = []
            while True:
                a = input("Введите числа, для завершения введите end")
                if a == "end":
                    break
                sm.append(int(a))
            if len(sm) == 0:
                return None
            return sum(sm) / len(sm)

    class Matrix:
        def __init__(self, rows, columns):
            self.rows = rows
            self.columns = columns
            self.data = [[0] * columns for _ in range(rows)]  # Инициализация матрицы нулями

        def set_value(self, row, col, value):
            if row >= self.rows or col >= self.columns:
                raise IndexError("Индекс вышел за границы")
            self.data[row][col] = value

        def get_value(self, row, col):
            if row >= self.rows or col >= self.columns:
                raise IndexError("Индекс вышел за границы")
            return self.data[row][col]

        def __str__(self):
            return "\n".join(["\t".join(map(str, row)) for row in self.data])







