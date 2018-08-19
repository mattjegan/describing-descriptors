class Person(object):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.capitalize()


p = Person('matt')
print(p.name)  # Matt

p.name = 'sam'
print(p.name)  # Sam
