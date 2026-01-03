import threading
from multiprocessing import Process
class FooBar:
    def __init__(self, n):
        self.n = n
        self.flag = True
        self.condition = threading.Condition()


    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            with self.condition:
                while not self.flag:
                    self.condition.wait()
                printFoo()
                self.flag = False
                self.condition.notify()



    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            with self.condition:
                while self.flag:
                    self.condition.wait()
                printBar()
                self.flag = True
                self.condition.notify()


def printFoo():
    print("foo", end="")

def printBar():
    print("bar", end="")

if __name__ == "__main__":
    fb = FooBar(5)
    t1 = threading.Thread(target=fb.foo, args=(printFoo,))
    t2 = threading.Thread(target=fb.bar, args=(printBar,))
    t1.start()
    t2.start()
    t1.join(); t2.join()
    # fb = FooBar(5)
    # p1 = Process(target=fb.foo)
    # p2 = Process(target=fb.bar)
    #
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
