from weakref import WeakKeyDictionary


class NonNegativeInteger(object):
    def __init__(self):
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data[instance]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f'{value} is not of type int')

        if value < 0:
            raise ValueError('Must be a non-negative integer')

        self.data[instance] = value


class Person(object):
    age = NonNegativeInteger()

p = Person()
p.age = 4       # OK
p.age = 0       # OK
p.age = 'matt'  # TypeError
p.age = -1      # ValueError
