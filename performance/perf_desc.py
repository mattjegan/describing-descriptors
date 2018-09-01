from weakref import WeakKeyDictionary
import time


class SimpleDesc:
    def __init__(self):
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data[instance]

    def __set__(self, instance, value):
        self.data[instance] = value


class Foo:
    bar = 0

def run_test_2(num):
    foo = Foo()
    start = time.time()

    for i in range(num):
        foo.bar += 1

    return time.time() - start
