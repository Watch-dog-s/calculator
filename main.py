from typing import Final
import math
import sys

class Calculator:
    # Константы
    PI: Final = 3.14
    E: Final =2.72
    PLUS_INFINITY = sys.float_info.max
    MINUS_INFINITY = -sys.float_info.max

    class Trigonometry:
        @staticmethod
        def sin(angle_radians):
            return math.sin(angle_radians)

        @staticmethod
        def cos(angle_radians):
            return math.cos(angle_radians)

        @staticmethod
        def tan(angle_radians):
            return math.tan(angle_radians)

    class StaticOperations:
        @staticmethod
        def add(a, b):
            return a + b

        @staticmethod
        def subtract(a, b):
            return a - b

        @staticmethod
        def multiply(a, b):
            return a * b

        @staticmethod
        def divide(a, b):
            if b == 0:
                raise ValueError("Division by zero is not allowed")
            return a / b

    class Matrix:
        def __init__(self, rows, columns):
            self.rows = rows
            self.columns = columns
            self.data = [[0] * columns for _ in range(rows)]  # Инициализация матрицы нулями

        def set_value(self, row, col, value):
            if row >= self.rows or col >= self.columns:
                raise IndexError("Index out of bounds")
            self.data[row][col] = value

        def get_value(self, row, col):
            if row >= self.rows or col >= self.columns:
                raise IndexError("Index out of bounds")
            return self.data[row][col]

        def __str__(self):
            return "\n".join(["\t".join(map(str, row)) for row in self.data])









