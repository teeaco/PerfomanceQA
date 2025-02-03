# Классы. Калькулятор
# Опишите класс Calculator, который будет реализовывать следующие методы и поля:
# sum(self, a, b) - сложение чисел a и b
# sub(self, a, b) - вычитание
# mul(self, a, b) - умножение
# div(self, a, b, mod=False) - деление. Если параметр mod == True, то метод должен возвращать остаток от деления вместо деления. По умолчанию mod=False.
# history(self, n) - этот метод должен возвращать строку с операцией по ее номеру относительно текущего момента (1 - последняя, 2 - предпоследняя). Формат вывода: sum(5, 15) == 20 (Не нужно форматировать результат операции). История операция своя у каждого объекта калькулятора.
# last - строка того же формата, что в предыдущем пункте, в которой содержится информация о последней операции по всем созданным объектам калькулятора. Т.е. это последняя операция последнего использованного объекта калькулятор. Если операций пока не было, то None.
# clear(cls) - метод, который очищает last, т.е. присваивает ему значение None.

class Calculator:
    last = None
    
    def __init__(self):
        self.history_log = []

    def sum(self, a, b):
        result = a + b
        operation = f"sum({a}, {b}) == {result}"
        self._log_operation(operation)
        return result

    def sub(self, a, b):
        result = a - b
        operation = f"sub({a}, {b}) == {result}"
        self._log_operation(operation)
        return result

    def mul(self, a, b):
        result = a * b
        operation = f"mul({a}, {b}) == {result}"
        self._log_operation(operation)
        return result

    def div(self, a, b, mod=False):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        if mod:
            result = a % b
            operation = f"div({a}, {b}) == {result}"
        else:
            result = a / b
            operation = f"div({a}, {b}) == {result}"
        self._log_operation(operation)
        return result

    def history(self, n):
        if 1 <= n <= len(self.history_log):
            return self.history_log[-n]
        else:
            return None

    @classmethod
    def clear(cls):
        cls.last = None

    def _log_operation(self, operation):
        self.history_log.append(operation)
        Calculator.last = operation
