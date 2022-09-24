from abc import ABC, abstractmethod

def addition(x,y):
    a = x + y
    return a

def subtraction(x,y):
    s = x - y
    return s

def multiplication(x,y):
    m = x*y
    return m

def division(x,y):
    d = x/y
    return d

class UtilityBase(ABC):
    @abstractmethod
    def addition(self):
        raise NotImplementedError

    @abstractmethod
    def subtraction(self):
        raise NotImplementedError

    @abstractmethod
    def multiplication(self):
        raise NotImplementedError

    @abstractmethod
    def division(self):
        raise NotImplementedError

class UtilityTool(UtilityBase):
    def __init__(self, variable1, variable2):
        self.compartment1 = variable1
        self.compartment2 = variable2

    def addition(self):
        return self.compartment1 + self.compartment2

    def subtraction(self):
        return self.compartment1 - self.compartment2

    def multiplication(self):
        return self.compartment1 * self.compartment2

    def division(self):
        return self.compartment1 / self.compartment2


class UtilityBelt(UtilityTool):
    def __init__(self, variable1, variable2):
        super(UtilityBelt, self).__init__(variable1, variable2)

    def power(self):
        return self.compartment1 ** self.compartment2

class DataSet:
    def __init__(self, input):
        self._data = input

    def __getitem__(self, item):
        return self._data.__getitem__(item)

    def __call__(self, item):
        return self._data[item]
