class Person(object):
    def __init__(self, name):
        self.name = name

    def __setattr__(self, attr, value):
        if attr == 'name':
            super().__setattr__(attr, value.capitalize())
        else:
            super().__setattr__(attr, value)


p = Person('matt')
print(p.name)  # Matt

p.name = 'sam'
print(p.name)  # Sam
