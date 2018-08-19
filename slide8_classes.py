class Person(object):
    def __init__(self, name):
        self.name = name

p = Person('matt')
print(p.name)  # matt

p.name = 'sam'
print(p.name)  # sam
