import concurrent.futures
import threading
## Best clean solution

class FooBar:
    def __init__(self, n: int):
        self.n = n
        self.foo_sem = threading.Semaphore(1)
        self.bar_sem = threading.Semaphore(0)

    def foo(self, printFoo):
        for _ in range(self.n):
            self.foo_sem.acquire()
            printFoo()
            self.bar_sem.release()

    def bar(self, printBar):
        for _ in range(self.n):
            self.bar_sem.acquire()
            printBar()
            self.foo_sem.release()


def printFoo():
    print("foo", end="")


def printBar():
    print("bar", end="")


if __name__ == "__main__":
    fb = FooBar(5)
    # t1 = threading.Thread(target=fb.foo, args=(printFoo,))
    # t2 = threading.Thread(target=fb.bar, args=(printBar,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executors:
        f1 = executors.submit(fb.foo, printFoo)
        f2 = executors.submit(fb.bar, printBar)

        f1.result()
        f2.result()
    # fb = FooBar(5)
    # p1 = Process(target=fb.foo)
    # p2 = Process(target=fb.bar)
    #
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
