from weakref import WeakKeyDictionary


class Person:
    def __init__(self, name):
        self.name = name

data = WeakKeyDictionary()
print(data.data)

p1 = Person('matt')
data[p1] = 1

p2 = Person('sam')
data[p2] = 2

print(data.data)

del p1
print(data.data)
