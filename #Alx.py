#Alx
import math

class Calculator:
    # Возведение в степень
    def power(self, base, exponent):
            return round(base ** exponent, 3)

    # Квадратный корень числа
    def square_root(self, number):
            if number < 0:
                return "Эй, от отрицательного числа корень искать не буду!"
            return round(math.sqrt(number), 3)

    # Среднее значение
    def average(self, numbers):
            if len(numbers) == 0:
                return "Список пуст"
            return round(sum(numbers) / len(numbers), 3)

    # Медиана
    def median(self, numbers):
            if len(numbers) == 0:
                return "Список пуст"
            sorted_numbers = sorted(numbers)
            n = len(sorted_numbers)
            mid = n // 2
            
            if n % 2 == 0:
                
                return round((sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2, 3)
            else:
                
                return round(sorted_numbers[mid], 3)
            
    # Десятичный логарифм
    def log10(self, number):
            if number <= 0:
                return "От отрицательного числа, не робит"
            return round(math.log10(number), 3)

    # Метод для выбора операции
    def calculate(self):
            # выбор операции
            operation = input("Выберите операцию (power, square_root, average, median, log10): ").strip()

            if operation == 'power':
                base = float(input("Введите основание: "))
                exponent = float(input("Введите степень: "))
                return f'Результат({base}, {exponent}): {self.power(base, exponent)}'
            
            elif operation == 'square_root':
                number = float(input("Введите число: "))
                return f'Результат({number}): {self.square_root(number)}'
            
            elif operation == 'average':
                numbers = list(map(float, input("Введите числа разделенные пробелами: ").split()))
                return f'Результат({numbers}): {self.average(numbers)}'
            
            elif operation == 'median':
                numbers = list(map(float, input("Введите числа разделенные пробелами: ").split()))
                return f'Результат({numbers}): {self.median(numbers)}'
            
            elif operation == 'log10':
                number = float(input("Введите число: "))
                return f'Результат({number}): {self.log10(number)}'
            
            else:
                return "Такого нет. Пожалуйста выберите из: power, square_root, average, median, log10."
        
# Проверка
calc = Calculator()
result = calc.calculate()
print(result)
