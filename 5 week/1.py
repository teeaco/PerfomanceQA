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
