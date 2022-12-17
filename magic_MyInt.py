class MyInt:
    def __init__(self, value):
        self.value = value

    @classmathod
    def validate(cls, other):
        return int(other) if isinstance(other, (str, int)) else other.value

    def __repr__(self):
        return f'{self.__class__} : {self.value}'

    def __str__(self):
        return f'{self.value}'

    def __add__(self, other):
        other = self.validate(other)
        return MyInt(self.value + other)
    
    def __sub__(self, other):
        other = self.validate(other)
        return MyInt(self.value - other)

    def __mul__(self, other):
        other = self.validate(other)
        return MyInt(self.value * other)

    def __truediv__(self, other):
        other = self.validate(other)
        return MyInt(self.value / other)
 
    def __eq__(self, other):
        other = self.validate(other)
        return self.value == other

    def __le__(self, other):
        other = self.validate(other)
        return self.value <= other

    def __It__(self, other):
        other = self.validate(other)
        return self.value < other

    def __ge__(self, other):
        other = self.validate(other)
        return self.value >= other

a = MyInt(5)
a = a + 5
print(a)

a = a - 2 - 3
a

a = a * '5'
print(a)

a = a / 10
print(a)
a 

a = MyInt(5)
print(a < 3)

print(a >= '3')

print(a == '5')
