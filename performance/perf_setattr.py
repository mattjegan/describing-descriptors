import time

class Foo:
    bar = 0

    def __setattr__(self, attr, value):
        if attr == 'bar':
            super().__setattr__('bar', value)
        else:
            super().__setattr__(attr, value)


def run_test_5(num):
    foo = Foo()
    start = time.time()

    for i in range(num):
        foo.bar += 1

    return time.time() - start
