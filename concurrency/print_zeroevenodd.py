import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.sem_zero = threading.Semaphore(1)
        self.sem_odd = threading.Semaphore(0)
        self.sem_even = threading.Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.sem_zero.acquire()
            printNumber(0)
            if (i % 2):
                self.sem_odd.release()
            else:
                self.sem_even.release()


    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.sem_even.acquire()
            printNumber(i)
            self.sem_zero.release()


    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.sem_odd.acquire()
            printNumber(i)
            self.sem_zero.release()


def printNumber(n: int):
    print(n, end='')


if __name__ == "__main__":
    fb = ZeroEvenOdd(5)
    t1 = threading.Thread(target=fb.zero, args=(printNumber,))
    t2 = threading.Thread(target=fb.even, args=(printNumber,))
    t3 = threading.Thread(target=fb.odd, args=(printNumber,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
