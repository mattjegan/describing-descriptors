import time

class Foo:
    _bar = 0

    @property
    def bar(self):
        return self._bar

    @bar.setter
    def bar(self, value):
        self._bar = value

def run_test_4(num):
    foo = Foo()
    start = time.time()

    for i in range(num):
        foo.bar += 1

    return time.time() - start
