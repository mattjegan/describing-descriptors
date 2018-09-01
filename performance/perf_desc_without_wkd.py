import time

class SimpleDesc:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[f'_{self.name}']

    def __set__(self, instance, value):
        instance.__dict__[f'_{self.name}'] = value

    def __set_name__(self, name, owner):
        self.name = name


class Foo:
    bar = 0


def run_test_1(num):
    foo = Foo()
    start = time.time()

    for i in range(num):
        foo.bar += 1

    return time.time() - start
