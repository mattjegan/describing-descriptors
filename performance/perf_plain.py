import time

class Foo:
    bar = 0

def run_test_3(num):
    foo = Foo()
    start = time.time()

    for i in range(num):
        foo.bar += 1

    return time.time() - start
