from weakref import WeakKeyDictionary


class CapitalizedValue(object):
    def __init__(self):
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data[instance]

    def __set__(self, instance, value):
        self.data[instance] = value.capitalize()


class Person(object):
    name = CapitalizedValue()

    def __init__(self, name):
        self.name = name


p = Person('matt')
print(p.name)  # Matt

p.name = 'sam'
print(p.name)  # Sam
