class BaseWallet:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def __str__(self):
        return f"{self.currency_name} Wallet {self.name} {self.amount}"
    
    def __add__(self, other):
        if isinstance(other, BaseWallet):
            converted_amount = other.amount * other.exchange_rate / self.exchange_rate
            return self.__class__(self.name, self.amount + converted_amount)
        elif isinstance(other, (int, float)):
            return self.__class__(self.name, self.amount + other)
        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        result = self + other
        self.amount = result.amount
        return self

    def __sub__(self, other):
        if isinstance(other, BaseWallet):
            converted_amount = other.amount * other.exchange_rate / self.exchange_rate
            return self.__class__(self.name, self.amount - converted_amount)
        elif isinstance(other, (int, float)):
            return self.__class__(self.name, self.amount - other)
        return NotImplemented

    def __rsub__(self, other):
        return -1 * (self - other)

    def __isub__(self, other):
        result = self - other
        self.amount = result.amount
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.name, self.amount * other)
        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.amount *= other
        return self

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.name, self.amount / other)
        return NotImplemented

    def __itruediv__(self, other):
        self.amount /= other
        return self

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.amount == other.amount

    def spend_all(self):
        if self.amount > 0:
            self.amount = 0

    def to_base(self):
        return self.amount * self.exchange_rate


class RubleWallet(BaseWallet):
    currency_name = "Ruble"
    exchange_rate = 1


class DollarWallet(BaseWallet):
    currency_name = "Dollar"
    exchange_rate = 60


class EuroWallet(BaseWallet):
    currency_name = "Euro"
    exchange_rate = 70
